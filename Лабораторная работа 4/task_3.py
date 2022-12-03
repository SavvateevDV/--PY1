def delete(list_, index=None):  # создаем функцию
    if index is None:  # если индекс не введен:
        list_ = list_[:-1]  # удаляется последний по индексу элемент из списка
    else:  # если индекс введен:
        list_ = list_[:index] + list_[index + 1:]  # соединяет левую и правую половину списка без индексируемого эл-та
    return list_  # возвращаем список

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
  # пустая строка