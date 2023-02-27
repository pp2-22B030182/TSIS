import re

txt = input()

li = txt.split()

for i in li:
    s = re.findall("^ab*",i)
    if s:
        print(i)