li = input()
def count1(x):
    cnt1 = 0
    for i in x:
        if i >= "A" and i <= "Z":
            cnt1 += 1
    return cnt1
def count2(x):
    cnt2 = 0
    for i in x:
        if i >= "a" and i <= "z":
            cnt2 += 1
    return cnt2
print( "Upper case letters:",count1(li))
print( "Lower case letters:",count2(li))