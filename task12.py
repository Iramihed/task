# Вычислить факториал введённого числа.
a=int(input("Ввелите число: "))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
print("Факториал числа", a, "равен", factorial)