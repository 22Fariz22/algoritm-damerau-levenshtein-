# -*- coding: utf-8 -*-


from transliterate.decorators import *
from transliterate import translit, get_available_language_codes,get_translit_function
from Algorythm_damerau.list_holodilniki import good_names


text_ru = 'айфон'

def transliterate_reverse(): # если слово киррилица,то переводим в латиницу и наоборот
    pass



print(translit(text_ru, 'ru',reversed=True))



