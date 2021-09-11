import math
import sys

srednee = 0
nums = []

with open(sys.argv[1]) as vvod :
    for line in vvod:
        nums.append(int(line))
        srednee += int(line)

srednee = math.ceil(srednee / len(nums))

shag = 0

for x in nums:
    while(x != srednee):
        if x > srednee:
            x -= 1
            shag +=1
        else:
            x += 1
            shag +=1

print(str(shag))