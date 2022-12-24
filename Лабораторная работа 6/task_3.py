OUTPUT_FILE = "output.csv"

def to_csv_file(filename, headers, rows, delimiter, new_line):  # задаем функцию с переменными
    with open(filename, 'w') as f:  # работаем в заданном вводными данными файле
        headers_line = ""  # создаем пустую строку для заголовков
        for h in headers:  # для переменной в списке с заголовками
            headers_line += h + delimiter  # добавляем элемент списка и разделитель
        headers_line = headers_line[:-1] + new_line  # удаляем запятую в конце строки и ставим отступ
        for n in rows:  # для переменной в списке со списками
            data_line = ""  # создаем пустую строку для данных
            for a in n:  # для переменной в списке из списка
                data_line += a + delimiter  # добавляем элемент списка и разделитель
            data_line = data_line[:-1] + new_line  # удаляем запятую в конце строки и ставим отступы
            headers_line += data_line  # соединяем заголовки и данные
        f.write(headers_line)  # записываем все в файл


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(OUTPUT_FILE, headers_list, data, ",", "\n")  # вызываем функцию с заданными аргументами


with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
