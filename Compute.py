n = int(input("Enter a number:"))
result = 0
for i in range(1, n+1):
    result += i/(i+1)
print(result)
