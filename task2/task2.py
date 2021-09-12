from math import sqrt

def func(x,y,xc,yc,r):
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r
f1 = open("f1.txt", "r")
content = f1.read()
f2 = open("f2.txt", "r")
content1 = f2.read()
if __name__ == '__main__':
    x=float(int(content1[0]))
    y=float(int(content1[1]))
    xc=float(int(content[0]))
    yc=float(int(content[1]))
    r=float(int(content[3]))
    func(x,y,xc,yc,r)
    if func(x, y, xc, yc, r):
        print("YES")
    else:
        print("NO")