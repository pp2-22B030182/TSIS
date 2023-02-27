import re

txt = input()

li = txt.split()

for i in li:
    s = re.findall("ab{2,3}$",i)
    if s:
        print(i)