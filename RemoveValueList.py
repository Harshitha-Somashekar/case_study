a = [12,24,35,24,88,120,155]
value = 24
for i in a:
    if i == value:
        a.pop(a.index(i))
print(a)