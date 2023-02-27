import re
txt = input().split()
for i in txt:
    s = re.findall("^a.+b$", i)
    if s:
        print(i)