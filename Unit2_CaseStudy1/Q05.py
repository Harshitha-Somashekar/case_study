string=input("Enter a string:")
outputString = ""
for i in range(len(string)):
    if i%2 == 0:
        outputString = outputString + string[i]
print(outputString)
