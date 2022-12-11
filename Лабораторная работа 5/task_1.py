from pprint import pprint  # импортируем функцию pprint из модуля pprint
array = []  # создаем пустой массив
for number in range(0, 16):  # для множества чисел от 1 до 15
    array.append({"bin":bin(number), "dec":number, "hex":hex(number), "oct":oct(number)})
    # добавляем в массив переведенные числа и текстовые обозначения к ним
pprint(array)  # печать массива через функцию pprint
# пустая строка