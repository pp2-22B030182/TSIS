#  1

def mygen(n):
    i = 1
    while(i < n):
        yield i*i
        i += 1

n = int(input())
a = mygen(n + 1)
for i in a:
    print(int(i))

# 2

def myGen(n):
    i = 0
    while(i <= n):
        if( i % 2 == 0):
            yield i
        i += 1

a = myGen(int(input()))

for i in a:
    print(int(i))
# 3

def geni(n):
    i = 0
    while(i < n):
        if(i % 3 == 0 and i % 4 == 0):
            yield i
        i += 1

a = geni(int(input()))

for i in a:
    print(int(i))

# 4

def MYGEN(n, m):
    i = n
    while(i <= m):
        yield i*i
        i += 1

a = int(input())
b = int(input())
x = MYGEN(a,b)

for i in x:
    print(int(i))


for i in range(a,b):
    print(int(i*i))
    


#  5

def gener(n):
    i = n
    while(i >= 0):
        yield i
        i -= 1

x = gener(int(input()))

for i in x:
    print(i)