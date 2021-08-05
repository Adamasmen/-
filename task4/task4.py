values = ["a", "z", "x", "y"]

x = 1
y = 10
z = 2
a = 9
shag=0

norm = (x+y+z+a)//4


for x in range(1, norm):
    if x > norm:
        x -= 1
        shag +=1
    else:
        x += 1
        shag +=1


for y in range(1, norm):
    if y > norm:
        y -= 1
        shag +=1

    else:
        y += 1
        shag +=1


for z in range(1, norm):
    if z > norm:
        z -= 1
        shag +=1

    else:
        z += 1
        shag +=1


for a in range(1, norm):
    if a > norm:
        a -= 1
        shag +=1
    else:
        a += 1
        shag +=1

print (shag)