import re
txt = input().split()
for i in txt:
    s = re.findall("^[A-Z][a-z]", i)
    if s:
        print(i)