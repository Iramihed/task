# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

from random import random
n=10
a=[]
l=int(input('нижняя гр масива:'))
h=int(input('верхняя гр масива:'))
for i in range(n):
    n=int(random()*(h-1))+1
    a.append(n)
print(a)
print('удаляемый деапазон')
l=int(input('нижняя гр:'))
h=int(input('верхняя гр:'))
i=0
m=n
while i<m:
    if l<=a[i]<=h:
        del a[i]
        m-=1
    else:

        i+=1
for i in range(m,n):
    a.append(0)
print(a)
