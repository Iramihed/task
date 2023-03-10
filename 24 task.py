# В единственной строке записан текст. Для каждого слова из данного текста
# подсчитайте, сколько раз оно встречалось в этом тексте ранее. Словом считается
# последовательность непробельных символов, идущих подряд. Слова разделены одним
# или большим числом пробелов или символами конца строки.    3 способа
text = input('Введите текст: ')
result = {}
# Разбивает строку на части, и проведем итерацию по каждому слову
for key in text.split():
    # Если слово уже встречалось, прибавим +1
    if not result.get(key) == None:
        result[key] += 1
        # Если не встречалось, присвоим ему ровно 1
    else:
        result[key] = 1
# Выводим результат
for key, value in result.items():
    print(f'Слово: {key}, Количество: {value}')