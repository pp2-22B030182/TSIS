import re 
s = input()
x = re.split('[_]', s)
print(x[0], end = '')
for i in range(1, len(x)):
    print(x[i].capitalize(), end = '')