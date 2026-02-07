#!/usr/bin/env python3
"""
Simple approach: Split multi-row INSERTs into single-row INSERTs
This makes boolean conversion much easier and more reliable
"""

import sys
import re

def split_and_convert(input_file, output_file):
    print(f"Processing {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change backticks to double quotes
    content = content.replace('`', '"')
    
    # Fix table name casing
    content = content.replace('"guestapp_', '"GuestApp_')
    content = content.replace('"myapp_', '"MyApp_')
    
    # Extract INSERT statements
    insert_pattern = r'INSERT INTO ("[^"]+"\s*\([^)]+\))\s*VALUES\s*(.+?);'
    
    skip_tables = [
        'django_session', 'auth_permission', 'auth_group',
        'django_content_type', 'django_migrations', 'django_admin_log'
    ]
    
    output_lines = []
    output_lines.append("-- Data-only import for PostgreSQL")
    output_lines.append("-- Run this in Supabase SQL Editor\n")
    output_lines.append("START TRANSACTION;\n")
    
    for match in re.finditer(insert_pattern, content, re.DOTALL):
        table_and_fields = match.group(1)
        values_part = match.group(2)
        
        # Check if we should skip this table
        skip = False
        for skip_table in skip_tables:
            if f'"{skip_table}"' in table_and_fields:
                skip = True
                break
        
        if skip:
            continue
        
        # Split multiple value sets: (...), (...), (...)
        # This regex finds each (...) group
        value_sets = re.findall(r'\([^)]+\)', values_part)
        
        # Create individual INSERT statements
        for value_set in value_sets:
            # Convert boolean values: , 0, -> , FALSE,  and , 1, -> , TRUE,
            # Also handle end of value set: , 0) -> , FALSE)
            value_set = re.sub(r',\s*0\s*,', ', FALSE,', value_set)
            value_set = re.sub(r',\s*1\s*,', ', TRUE,', value_set)
            value_set = re.sub(r',\s*0\s*\)', ', FALSE)', value_set)
            value_set = re.sub(r',\s*1\s*\)', ', TRUE)', value_set)
            # Handle start: (0, -> (FALSE,
            value_set = re.sub(r'\(\s*0\s*,', '(FALSE,', value_set)
            value_set = re.sub(r'\(\s*1\s*,', '(TRUE,', value_set)
            
            output_lines.append(f"INSERT INTO {table_and_fields} VALUES {value_set};")
    
    output_lines.append("\nCOMMIT;")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"✅ Created {len(value_sets)} INSERT statements")
    print(f"✅ Output saved to: {output_file}")
    print(f"\nNext steps:")
    print(f"1. Open {output_file}")
    print(f"2. Copy all contents")
    print(f"3. Go to Supabase Dashboard → SQL Editor")
    print(f"4. Paste and click 'Run'")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python split_inserts.py input.sql output.sql")
        sys.exit(1)
    
    try:
        split_and_convert(sys.argv[1], sys.argv[2])
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
