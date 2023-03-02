li = input().split()
def umnozhenie(x):
    y = 1
    for i in x:
        y *= int(i)
    return y
print(umnozhenie(li))