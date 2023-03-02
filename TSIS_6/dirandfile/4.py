import os

file = open("a.txt",'r')
content = file.read()

cnt = 0 
for i in content:
    if i == "\n":
        cnt += 1
print(cnt + 1)