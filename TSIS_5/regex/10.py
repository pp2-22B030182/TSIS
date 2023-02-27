import re
x = input()
s = re.sub(r"(\w)([A-Z])",r"\1_\2",x)
y = s.lower()
print(y)