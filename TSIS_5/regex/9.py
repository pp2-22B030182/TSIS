import re
x = input()
s = re.sub(r"( )([A-Z])",r"\1 \2",x)
print(s)