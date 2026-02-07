import re
import os

def convert_mysql_to_postgres(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output = []
    output.append("-- Supabase DB Reset & Recreate Script")
    output.append("-- Generated for BioBinConnect\n")
    output.append("DROP SCHEMA public CASCADE;")
    output.append("CREATE SCHEMA public;")
    output.append("GRANT ALL ON SCHEMA public TO postgres;")
    output.append("GRANT ALL ON SCHEMA public TO public;\n")
    output.append("SET search_path TO public;\n")

    current_table = ""
    in_insert = False
    insert_table = ""
    insert_fields = ""
    insert_values = []

    # Patterns
    table_pattern = re.compile(r'CREATE TABLE IF NOT EXISTS `([^`]+)` \(')
    insert_start_pattern = re.compile(r'INSERT INTO `([^`]+)` \(([^)]+)\) VALUES', re.I)
    
    # Track boolean columns for each table
    boolean_cols = {
        'guestapp_collector': ['is_active'],
        'guestapp_compostmanager': ['is_active'],
        'guestapp_customuser': ['is_superuser', 'is_verified', 'is_active', 'is_staff'],
        'guestapp_passwordresetotp': ['is_used'],
        'guestapp_farmer': ['is_active'],
        'myapp_tbl_compostbatch': ['salary_paid'],
        'myapp_tbl_wasteinventory': ['salary_paid']
    }

    # Mapping MySQL types to Postgres
    type_map = [
        (re.compile(r'\bint\s+NOT\s+NULL\s+AUTO_INCREMENT\b', re.I), 'SERIAL'),
        (re.compile(r'\bbigint\s+NOT\s+NULL\s+AUTO_INCREMENT\b', re.I), 'BIGSERIAL'),
        (re.compile(r'\bint\s+NOT\s+NULL\b', re.I), 'INTEGER NOT NULL'),
        (re.compile(r'\bint\s+DEFAULT\s+NULL\b', re.I), 'INTEGER DEFAULT NULL'),
        (re.compile(r'\bbigint\s+NOT\s+NULL\b', re.I), 'BIGINT NOT NULL'),
        (re.compile(r'\bbigint\s+DEFAULT\s+NULL\b', re.I), 'BIGINT DEFAULT NULL'),
        (re.compile(r'\btinyint\(1\)\s+NOT\s+NULL\b', re.I), 'BOOLEAN NOT NULL'),
        (re.compile(r'\btinyint\(1\)\s+DEFAULT\s+NULL\b', re.I), 'BOOLEAN DEFAULT NULL'),
        (re.compile(r'\blongtext\b', re.I), 'TEXT'),
        (re.compile(r'\bdatetime\(6\)', re.I), 'TIMESTAMP(6)'),
        (re.compile(r'\bdate\b', re.I), 'DATE'),
        (re.compile(r'\btime\(6\)', re.I), 'TIME(6)'),
        (re.compile(r'\bvarchar\b', re.I), 'VARCHAR'),
        (re.compile(r'\bsmallint\s+UNSIGNED\b', re.I), 'SMALLINT'),
        (re.compile(r'\bdecimal\b', re.I), 'DECIMAL')
    ]

    def process_values(table, fields, values_str):
        field_list = [f.strip().strip('"').lower() for f in fields.split(',')]
        table_bool_cols = boolean_cols.get(table.lower(), [])
        
        # Split values intelligently (handling quoted strings with commas)
        # This is a basic split that handles single-quoted strings
        parts = []
        current = []
        in_quotes = False
        for char in values_str:
            if char == "'":
                in_quotes = not in_quotes
                current.append(char)
            elif char == ',' and not in_quotes:
                parts.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        parts.append(''.join(current).strip())
        
        if len(parts) != len(field_list):
            return values_str # Fallback if splitting fails
            
        new_parts = []
        for i, val in enumerate(parts):
            if field_list[i] in table_bool_cols:
                if val == '0': new_parts.append('FALSE')
                elif val == '1': new_parts.append('TRUE')
                else: new_parts.append(val)
            else:
                new_parts.append(val)
        return ', '.join(new_parts)

    for line in lines:
        cleaned_line = line.strip()
        
        # Handle Insert Values continuing on next lines
        if in_insert:
            val_match = re.search(r'\((.*?)\)(?:,|$|;)', cleaned_line)
            if val_match:
                v_set = val_match.group(1)
                v_set = process_values(insert_table, insert_fields, v_set)
                output.append(f'INSERT INTO "{insert_table}" ({insert_fields}) VALUES ({v_set});')
            
            if cleaned_line.endswith(';'):
                in_insert = False
            continue

        if not cleaned_line or cleaned_line.startswith('--') or cleaned_line.startswith('/*') or cleaned_line.startswith('SET ') or cleaned_line.startswith('START TRANSACTION') or cleaned_line.startswith('COMMIT'):
            continue

        # Table Creation
        table_match = table_pattern.search(line)
        if table_match:
            table_name_orig = table_match.group(1)
            current_table = table_name_orig.lower()
            table_name = table_name_orig
            if table_name.startswith('guestapp_'): table_name = table_name.replace('guestapp_', 'GuestApp_')
            if table_name.startswith('myapp_'): table_name = table_name.replace('myapp_', 'MyApp_')
            
            output.append(f'\nDROP TABLE IF EXISTS "{table_name}" CASCADE;')
            output.append(f'CREATE TABLE "{table_name}" (')
            continue

        if current_table and cleaned_line.startswith('`'):
            col_match = re.search(r'^`([^`]+)`\s+(.*)$', cleaned_line)
            if col_match:
                col_name = col_match.group(1)
                col_def = col_match.group(2).rstrip(',')
                
                # Apply type mappings
                for pattern, p_type in type_map:
                    if pattern.search(col_def):
                        col_def = pattern.sub(p_type, col_def)
                        break
                
                output.append(f'  "{col_name}" {col_def},')
            continue

        if current_table and cleaned_line.startswith('PRIMARY KEY'):
            pk_match = re.search(r'PRIMARY KEY \(`([^`]+)`\)', cleaned_line)
            if pk_match:
                pk_col = pk_match.group(1)
                output.append(f'  CONSTRAINT "{current_table}_pk" PRIMARY KEY ("{pk_col}")')
            continue

        if current_table and cleaned_line.startswith('UNIQUE KEY'):
            uk_match = re.search(r'UNIQUE KEY `([^`]+)` \(([^)]+)\)', cleaned_line)
            if uk_match:
                uk_name_orig = uk_match.group(1)
                uk_name = f"{table_name}_{uk_name_orig}"
                uk_cols = uk_match.group(2).replace('`', '"')
                if not output[-1].endswith(','):
                    output[-1] += ','
                output.append(f'  CONSTRAINT "{uk_name}_unique" UNIQUE ({uk_cols})')
            continue

        if current_table and (re.search(r'^\)\s*;?$', cleaned_line) or cleaned_line.startswith(') ENGINE=')):
            if output[-1].endswith(','):
                output[-1] = output[-1].rstrip(',')
            output.append(');')
            current_table = ""
            continue

        # Data Insertion Start
        insert_match = insert_start_pattern.search(line)
        if insert_match:
            it_table_orig = insert_match.group(1)
            insert_table = it_table_orig
            if insert_table.startswith('guestapp_'): insert_table = insert_table.replace('guestapp_', 'GuestApp_')
            if insert_table.startswith('myapp_'): insert_table = insert_table.replace('myapp_', 'MyApp_')
            
            insert_fields = insert_match.group(2).replace('`', '"')
            in_insert = True
            
            # Check if values are on the same line
            values_start = line.find('VALUES') + 7
            values_part = line[values_start:].strip()
            if values_part:
                value_sets = re.findall(r'\((.*?)\)(?:,|$|;)', values_part)
                for v_set in value_sets:
                    v_set = process_values(insert_table, insert_fields, v_set)
                    output.append(f'INSERT INTO "{insert_table}" ({insert_fields}) VALUES ({v_set});')
                if values_part.endswith(';'):
                    in_insert = False
            continue

    final_content = '\n'.join(output)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    convert_mysql_to_postgres('d:\\All Projectssss\\Main Project\\BioBinConnect\\MyProject\\db_biobinconnect.sql', 'd:\\All Projectssss\\Main Project\\BioBinConnect\\MyProject\\supabase_reset.sql')
    print("Conversion complete: supabase_reset.sql created.")
