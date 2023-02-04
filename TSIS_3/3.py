def solve(numheads,numlegs):
    r = (legs - 2*h) / 2
    c = h - r
    return r, c

h = 35
legs = 94
print(*solve(h,legs))