#Найти все числа, кратные 11, в диапазоне от 0 до 10000.

a=int(input("Введите число от диапазона: "))
b=int(input("Введите число до диапазона: "))
n=int(input("Введите число кратное:" ))
for i in range(a,b+1):
    if (i % n == 0):
        print(i)