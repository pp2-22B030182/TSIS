# 1

def ounces(grams):
    return 28.3495231 * grams

grams = float(input())

print(ounces(grams))

# 2
def faran(cels):
    return (cels-32) * (5 / 9) 
    
cels = float(input())

print(faran(cels))

# 3

def solve(numheads,numlegs):
    r = (legs - 2*h) / 2
    c = h - r
    return r, c

h = 35
legs = 94
print(*solve(h,legs))


# 4
import math

li = input().split()    


def isprime(num):
    if(num == 1):
        return False
    for i in range (2, int(math.sqrt(num)) + 1):
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


# 5
from itertools import permutations
st = input()


def permutate(string):
    for i in permutations(string):
        print(''.join(i))


permutate(st)


# 6
def reverse(sentence):
    word = sentence.split()
    revword = word[::-1]
    print(" ".join(revword))

sentence = "We are ready"
reverse(sentence)

# 7
def check(li):
    i = 0
    while i != li.__len__() :
        if li[i] == 3 and i+1 != li.__len__() :
                if li[i+1]==3 :
                    return True 
    return False

# 8
def checkSpy(li):
    i = 0
    while i != li.__len__() :
        if li[i] == 0:
            k = i
            while k != li.__len__():
                if li[k] == 0:
                    o = k
    
                    while o != li.__len__():
                        if li[o] == 7 :
                            return True    
                        o+=1
                k+=1
        i+=1
    return False
# 9
def volume(rad):
    return (4/3)*math.pi* ( rad * rad * rad)

# 10

def uniq(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
    return li1

# 11
def isPalindrom(s):
    i = 0
    while i != math.ceil(s.__len__() / 2):
        if s[i] != s[s.__len__()-i-1]:
            return False
        i+=1
    return True

# 12
def histogram(li):
    for i in li:
        for k in range(i):
            print('*',end='')
        print()

# 13
import random

def guess_game():
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    snums = random.randint(1,20)
    for i in range (1,7):
        print("Take a guess.")
        g = int(input())
        if g == snums:
            print("Good job, " + name + "! You guessed my number in " + str(i) + " guesses!")
        elif g < snums:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    else:
        print("No. The number I was thinking of was " + str(snums))

guess_game()