from math import sqrt
import sys

def func(x,y,xc,yc,r):
    coord = (x - xc) * (x - xc) + (y - yc) * (y - yc) 
    if coord == r * r :
        print(0)
    elif coord < r * r :
        print(1)
    else: 
        print(2)
f1 = open(sys.argv[1], "r")
content = f1.readline()
xc=float(content.split()[0])
yc=float(content.split()[1])
content = f1.readline()
r=float(content)
with open(sys.argv[2], "r") as f2:
    for line in f2 :
        x=float(line.split()[0])
        y=float(line.split()[1])
        func(x, y, xc, yc, r)



