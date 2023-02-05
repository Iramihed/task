#Придумать и обработать исключения на TypeError и ValueError.

try:
    a=34/"10"
except TypeError:
    print("Типы данных делить нельзя")
    try:
        n=print(int("34 10"))
    except ValueError:
        print("Данныу не могут быть преобразованны в число")
else:
    print("Ошибок нет")
finally:
    print("Конструкция сработала")