import math

li = input().split()


def isprime(num):
    if(num == 1):
        return False
    for i in range (2, int(math.sqrt(num)) + 1):     # 1 2 3 4 5 6
        if(num % i == 0):
            return False
    return True 


def prime(li):
    res = []
    for num in li:
        num = int(num)
        if(isprime(num) == True):
            res.append(num)
    return res

print(prime(li))