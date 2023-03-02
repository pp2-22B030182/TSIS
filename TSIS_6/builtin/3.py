li = input()
def polin(x):
    if x == x[::-1]:
        return True
    else:
        return False

if polin(li):
    print("Yes, it is polindrome")
else:
    print("No, it isn't polindrome")