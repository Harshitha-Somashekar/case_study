a = [12,24,35,24,88,120,155,88,120,155]
a.reverse()
for i in a:
    if a.count(i) > 1:
        a.remove(i)
a.reverse()
print(a)
