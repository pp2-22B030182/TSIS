import re

txt = input()

li = txt.split()

for i in li:
    s = re.findall("^a.+b$",i)
    if s:
        print(i)