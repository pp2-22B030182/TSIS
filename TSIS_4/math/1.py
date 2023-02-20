# 1
import math

x = float(input())

radian = math.radians(x)

print(radian)

# 2
import math

h = float(input())
a = float(input())
b = float(input())
s = (a + b)/2 * h
print(s)

# 3
import math
n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
S = ( n * a**2 ) / 4 * math.tan(math.pi / n)
print("The area of the polygon is:", S)

# 4
import math

a = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
S = a * h
print("Expected Output:",S)