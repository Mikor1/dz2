import random
b = []
n = int(input('Введите количество элементов: '))
for i in range(n):
     b.append( random.randint(-100, 100))
print(b)