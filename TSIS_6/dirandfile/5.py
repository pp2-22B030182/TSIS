import os

mylist = input().split()

with open('5.1.txt','w')as wr:
    for i in mylist:
        wr.write('%s ' %i)