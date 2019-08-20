import math
a = [2, -5, 8, 9, -25, 25, 4]
b = []
for i in a:
    if i > 0 and math.sqrt(i) % 1 == 0:
        b.append(int(math.sqrt(i)))
print(b)
