# 1
class stringer:
    def __init__(self, string):
       self.string = string
    def getString(self):
        self.string = str(input())
    def printString(self):
        print(self.string.upper())

#2 task 
class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length)        
#3

class Rectangle(Shape):

    def __init__(self,  width):
        self.width = width

    def area (self, w):
        print( self.length  * w)  

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
class bank:
    def __init__(self, name  , balance = 0 ):
        self.name  = name
        self.balance  = balance
    def plus(self,add):
        self.balance = self.balance+add
        print('balance of',self.name,':',self.balance)
    def denote(self,min):
        if min > self.balance:
            print("nehvatka")
        else:
            self.balance = self.balance - min
            print('balance of',self.name,':',self.balance)

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
