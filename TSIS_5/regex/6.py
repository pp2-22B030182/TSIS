import re
txt = input()
s = re.sub("[ ,.]" , ":", txt)
print(s)