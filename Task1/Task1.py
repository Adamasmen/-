
import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
count = 0
while count != 1:
    if count == 0:
        count = 1
    print(count)
    count = count + m - 1
    if count > n:
        count = count - n