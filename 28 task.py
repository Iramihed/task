#В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить
# количество символов и слов в ней.
f = open("Next26.txt","r",encoding="utf-8")
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i,len(i.replace("\n","")),'симв.',word,'сл.')
print('строк в тексте - ',line)
f.close()




