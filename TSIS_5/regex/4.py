import re

txt = input()

li = txt.split()

for i in li:
    s = re.findall("^[A-Z][a-z]",i)
    if s:
        print(i)