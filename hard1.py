a = 'y = -12x + 11111140.2121'
x = 2.5
b = a.split(' ')
d = str(b[2])
b[2] = d[:-1]
c = float(b[2]) * x + float(b[4])
print(c)