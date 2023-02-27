import re
txt = input().split()
for i in txt:
    s = re.findall("ab{2,3}$", i)
    if s:
        print(i)