#!/usr/bin/env python3

a = ()          # Создание пустого кортежа через литерал
print(a)        # Выведет: ()
print(type(a))  # Выведет: <class 'tuple'>

a = 'a',        # При объявлении через литерал кортежа, состоящего из одного элемента, запятая после элемента обязательна
print(a)        # Выведет: ('a',)

a = ('a', )     # То же, что на строке 7. Признаком литерала кортежа является запятая после единственного элемента, а не скобки
print(a)        # Выведет: ('a',)

a = ('a')       # Если не добавить запятую после единственного элемента, выражение распознаётся как строка в скобках, а не как кортеж
print(a)        # Выведет строку: a

a = 'abcdef',   # Хотя строка — последовательность символов (итерируемый объект), она распознаётся как один элемент
print(a)        # Выведет: ('abcdef',)

a = 'a', 'b', 'c', 'd', 'e', 'f'    # При объявлении кортежа, состоящего более чем из одного элемента, завершающая запятая не обязательна
print(a)                            # Выведет: ('a', 'b', 'c', 'd', 'e', 'f')

a = ('a', 'b', 'c', 'd', 'e', 'f')  # То же, что на строке 19, только литерал кортежа заключён в скобки
print(a)                            # Выведет: ('a', 'b', 'c', 'd', 'e', 'f')

a = (                               # То же, что на строке 22, только каждый элемент кортежа объявлен на новой строке
    'a',
    'b',
    'c',
    'd',
    'e',
    'f'
)
print(a)                            # Выведет: ('a', 'b', 'c', 'd', 'e', 'f')

a = ('a', 'b' 'c', 'd' 'e' 'f')     # Если не ставить запятую между строками, интерпретатор объединяет эти строки
print(a)                            # Выведет: ('a', 'bc', 'def')

a = (                               # То же, что на строке 35, только литералы строки разделены не пробелами,
    'a',                            # а символом перехода на новую строку
    'b'
    'c',
    'd'
    'e'
    'f'
)
print(a)                            # Выведет: ('a', 'bc', 'def')

a = tuple()                         # Создание пустого кортежа через вызов функции без аргументов
print(a)                            # Выведет: ()

a = tuple('abcdef')                 # Создание кортежа через вызов функции на основе итерируемого объекта (строки)
print(a)                            # Выведет: ('a', 'b', 'c', 'd', 'e', 'f')
