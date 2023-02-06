# Вычислить количество отрицательных элементов под главной диагональю матрицы.
from random import randint as rand
import numpy as np
a = []
for i in range(4):
    c = []
    [c.append(rand(-10, 10)) for x in range(4)]
    a.append(c)
    print(c)
count = 0
for i in range(4):
    for x in range(i):
        if a[i][x] < 0:
            print(a[i][x])
            count+=1
print("",count)
