a = [12,24,35,70,88,120,155]
a = [i for j, i in enumerate(a) if i%5 != 0 and i%7 != 0]
print(a)
