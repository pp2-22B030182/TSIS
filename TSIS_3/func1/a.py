# 1

def ounces(grams):
    return 28.3495231 * grams

grams = float(input())

print(ounces(grams))

# 2
def faran(cels):
    return (cels-32) * (5/9) 
    
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
def has_33(nums):
    for i in range(0,len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
        
    return False
        
nums = input().split()
        
has_33(nums)
# 8
def spy_game(nums):
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                if nums[j] == 0:
                    for x in range(j+1, len(nums)):
                        if (nums[x] == 7):
                            return True
        
nums = input().split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

if spy_game(nums) == True:
    print("True")
else:
    print("False")
# 9
import math
def volume(rad):
    return (4/3)*math.pi* ( rad * rad * rad)


rad = float(input())
print(volume(rad))


# 10

def uniq(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
    return li1

li = input().split()
print(uniq(li))

# 11
def isPalindrom(s):
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

s = input()
isPalindrom(s)

# 12
def histogram(li):
    for i in li:
        i = int(i)
        for k in range(i):
            k = int(k)
            print('*',end ='')
        print()

li = input().split()
histogram(li)


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
            break
        elif g < snums:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    else:
        print("No. The number I was thinking of was " + str(snums))

guess_game()