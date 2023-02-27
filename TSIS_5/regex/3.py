import re
txt = input().split()
for i in txt:
    s = re.findall("[a-z]_[a-z]", i)
    if s:
        print(i)