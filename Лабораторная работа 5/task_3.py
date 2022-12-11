import random  # импортируем модуль random


def get_unique_list_numbers() -> list[int]:  # создаем функцию
    array = []  # создаем пустой массив
    while len(array) < 15:  # создаем цикл пока не составим строку из 15 символов
        rand_num = random.randint(-10, 10)  # переменная со случайным натуральным числом от -10 до 10
        if rand_num not in array:  # если добавляемый символ новый
            array.append(rand_num)  # добавляем символ
    return array  # возвращаем массив с символами


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# пустая строка
