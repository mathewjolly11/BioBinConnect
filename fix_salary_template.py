import re

# Fix manager_salaries.html
with open(r'd:\All Projectssss\Main Project\BioBinConnect\MyProject\templates\Admin\manager_salaries.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all instances of period_filter== to period_filter ==
content = re.sub(r"period_filter=='", "period_filter == '", content)

with open(r'd:\All Projectssss\Main Project\BioBinConnect\MyProject\templates\Admin\manager_salaries.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed manager_salaries.html")
