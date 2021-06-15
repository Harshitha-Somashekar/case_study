a = [12,24,35,24,88,120,155]
value = [24]
a = [i for j, i in enumerate(a) if i not in value]
print(a)
