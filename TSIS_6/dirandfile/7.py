import os

with open('5.1.txt','r')as re:
    content = re.read()
with open(input(),'w') as wr:
    wr.write(content)