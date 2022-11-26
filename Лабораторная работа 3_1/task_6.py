list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_num = 0  # максимальный элемент

for current in range(len(list_numbers)):  # поиск положения последнего максимального элемента
    if list_numbers[current] >= max_num:  # если элемент у текущего индекса равен максимальному элементу, то:
        max_num = list_numbers[current]  # максимальный элемент равен текущему элементу
        max_current = current  # индекс максимального элемента равен текущему индексу

last_, last_max = list_numbers[len(list_numbers) - 1], list_numbers[max_current]  # переменные искомых элементов
list_numbers[len(list_numbers) - 1], list_numbers[max_current] = last_max, last_  # замена  элементов

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
  #