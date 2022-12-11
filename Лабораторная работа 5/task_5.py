import random  # импортируем модуль random


def get_random_password(n=8) -> str:  # создаем функцию заданной длины (по умолчанию 8 символов)
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' * n
    # создаем перечень символов для пароля с домножением на n для возможности дублирования символов
    return ''.join(random.sample(a, n))  # возвращаем строку с паролем длиной n символов


print(get_random_password())  # печатаем функцию
# пустая строка