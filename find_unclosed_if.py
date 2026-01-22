import re

with open(r'd:\All Projectssss\Main Project\BioBinConnect\MyProject\templates\Admin\waste_sales.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

if_stack = []
for i, line in enumerate(lines, 1):
    # Find all {% if ... %} tags
    if_matches = re.findall(r'{%\s*if\s+', line)
    elif_matches = re.findall(r'{%\s*elif\s+', line)
    else_matches = re.findall(r'{%\s*else\s*%}', line)
    endif_matches = re.findall(r'{%\s*endif\s*%}', line)
    
    for match in if_matches:
        if_stack.append(('if', i, line.strip()))
    
    for match in endif_matches:
        if if_stack:
            if_stack.pop()
        else:
            print(f"Line {i}: Extra endif without matching if")
            print(f"  {line.strip()}")

print(f"\nTotal unclosed if statements: {len(if_stack)}")
if if_stack:
    print("\nUnclosed if statements:")
    for tag_type, line_num, line_content in if_stack:
        print(f"Line {line_num}: {line_content}")
