# 1
class String():

    def getString(self):
        d = input()
        return d

    def printString(self):
        print(self.getString().upper())

s = String()
s.printString()

# 2
class Shape():
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length**2
    
s = Shape()
# 3

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

d = Rectangle(int(input()), int(input()))

print(d.area())
# 4
import math

class point:
    def __init__(self, x = 5  , y = 9 ):
        self.x  = x
        self.y  = y

    def show(self):
        print(f'{self.x}'+ ' '+ f'{self.y}')

    def move(self, x , y):
        self.x = x
        self.y = y
        print('New coor:',self.x,self.y)

    def dist(self,x,y):
        d = math.sqrt(pow((self.x - x),2) + pow((self.y - y),2))
        print(d)



#5
class Account():
    def __init__(self, owner, bal):
        self.owner = owner
        self.bal = bal
    def deposit(self, sum):
        self.bal += sum
    def withdraw(self, sum):
        if self.bal < sum:
            print("No enough money")
        else:
            self.bal -= sum

a = Account("Maksat", 100000)
a.deposit(1000)
a.withdraw(100)
print(a.bal)

#6
def isPrime(x):
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d == 0:
        return False
    else: 
        return True

def filt(li):
    print(list(map(lambda x : isPrime(x), li)))
    print(list(filter(isPrime, [1, 3, 2,5 , 20, 21])))
