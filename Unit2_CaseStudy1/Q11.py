a = [12,24,35,70,88,120,155]
index = (0,4,5)
a = [i for j, i in enumerate(a) if j not in index]
print(a)
