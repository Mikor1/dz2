a = [1, 3, 5, 6, 8]
c = []
for i in range(len(a)):
    if a[i]%2==0:
        c.append(a[i]/4)
    else:
        c.append(a[i]*2)
print(c)
