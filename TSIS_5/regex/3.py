import re

txt = input()

li = txt.split()

for i in li:
    s = re.findall("[a-z]_[a-z]",i)
    if s:
        print(i)