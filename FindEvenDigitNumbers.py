num1 = 1000
num2 = 3000
numberList = []
for i in range(num1, num2 + 1):
    numberList.append(i)
    for j in str(i):
        if int(j)%2 != 0:
            numberList.remove(i)
            break
print(numberList)
