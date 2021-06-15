import random

num1 = 1
num2 = 1000
randomlist = []
listLen = 5
while len(randomlist) != listLen:
    n = random.randint(num1, num2 + 1)
    if n%5 == 0 or n%7 == 0:
        randomlist.append(n)
print(randomlist)
