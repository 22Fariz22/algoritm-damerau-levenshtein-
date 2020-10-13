# -*- coding: utf-8 -*-
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance_ndarray
from Algorythm_damerau.list_holodilniki import holodolniki,list_of_goods

# вставляем в words итерируемый список брендов в цикле for
# (holodilniki я импортировал из list_holodilniki.py)
def fix_command(text, words=[i for i in holodolniki]):
    import numpy as np
    array = np.array(words)

    # result это лист c кортежами
    result = list(zip(words, list(normalized_damerau_levenshtein_distance_ndarray(text, array))))

    command, rate = min(result, key=lambda x: x[1])

    # значение которое можно регулировать допустимое количество ошибок
    if rate > 0.45:
        return

    return command

# все что ниже этой строки не будет импортироватся.
if __name__ == '__main__':
    count = 0   # количество None(то есть не распознанных объектов)
    num_of_good = len(list_of_goods)  # количество name_good

    # циклом for проходим по списку name_good и вставляем элемент в функцию алгоритма
    for i in list_of_goods:
        print(fix_command(i), f": {i} ",)
        if fix_command(i) is None:  #считаем None
            count += 1


    print(f"Всего good_name:", len(list_of_goods))
    print("Из них распознано:", len(list_of_goods)-count)
    print("Процент распознанных товаров:", round((len(list_of_goods)-count) / (len(list_of_goods)/100),1),"%")



