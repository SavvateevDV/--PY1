import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:  # задаем функцию
    with open(filename, 'r') as f:  # открываем файл для чтения
        headers = f.readline().split(",")  # переносим заголовки
        headers[-1] = headers[-1][0: -1]  # удаляем символы переноса
        list_ = []  # создаем пустой список
        while True:  # формируем список
            data = {}  # создаем пустой словарь
            numbers = f.readline().split(",")  # переносим данные
            numbers[-1] = numbers[-1][0:-1]  # удаляем символы переноса
            if not numbers[0]:  # остановить когда закончатся пеерносимые данные
                break
            for i in range(len(headers)):  # для каждого элемента данных
                data[headers[i]] = numbers[i]  # соединяем заголовки и данные
            list_.append(data)  # добавляем все в список
    return list_  # возвращаем список
csv_to_list_dict(INPUT_FILE)

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
