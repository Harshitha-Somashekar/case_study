number=input("Enter the number:")
factors = []
for i in range(1,int(number)):
    if int(number)%i == 0:
        factors.append(i)
print("Factors of " + number +" : " + str(factors))
for i in factors:
    if i%2 == 0:
        print("Factor " + str(i) + " is even")
    else:
        print("Factor " + str(i) + " is odd")
