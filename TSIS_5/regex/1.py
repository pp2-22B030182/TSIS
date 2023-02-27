import re

txt = input().split()
for i in txt:
    s = re.findall("^ab*", i)
    if s:
        print(i)