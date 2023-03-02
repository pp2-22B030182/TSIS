import math
import time
number = int(input())
miliseconds = int(input())
def sqr(x):
    n = math.sqrt(x)
    return n
n = miliseconds/1000
time.sleep(n)
print("Square root of", number, "after", miliseconds, "miliseconds is", sqr(number))