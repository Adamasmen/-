
n = int(input("n: "))
m = int(input("m: "))
count = 0
while count != 1:
    if count == 0:
        count = 1
    print(count)
    count = count + m - 1
    if count > n:
        count = count - n