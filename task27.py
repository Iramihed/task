#Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка.

fname= input('Файл: ')
fname2= input('Файл: ')
fname3= input('Файл: ')
fname4= input('Файл: ')
f=open("text.txt", "w")
f.write(fname)
f.write(fname2)
f.write(fname3)
f.write(fname4)