#Найти сумму элементов, находящихся между
#минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.
import random

a = [random.randint(1, 50) for i in
     range(10)]  # генератор списка, элемент выбирается случайно в диапазоне от 1 до 50. всех элементов 10

print(a)

min_i = a.index(min(a))
max_i = a.index(max(a))

print(min_i, max_i)
s = 0
for i in range(min_i + 1, max_i):
    print(a[i])
    s += a[i]
print('sum ', s)