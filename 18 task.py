# В одномерном массиве целых чисел определить
# два наименьших элемента. Они могут быть как
# равны между собой (оба являться минимальными),
# так и различаться.

from random import randint
array=[randint(1,20)for i in range(10)]
print("Массив целых чисел: ",array)
min1=min(array)
array.remove(min1)
min2=min(array)
print("Первый наименьший элемент: ",min1)
print("Второй наименьший элемент: ",min2)