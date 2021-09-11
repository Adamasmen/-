from math import sqrt
import sys

def func(x,y,xc,yc,r):
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r

nums = []

with open(sys.argv[1]) as vvod1 :
    for line in vvod1:
        nums.append(int(line))
        xc=(int[0])
        yc=(int[1])
        r=(int[3])

numbs = []

with open(sys.argv[2]) as vvod2 :
    for line in vvod2:
        numbs.append(int(line))
        x=(int[0])
        y=(int[1])
        func(x,y,xc,yc,r)
    if func(x, y, xc, yc, r):
        print("YES")
    else:
        print("NO")