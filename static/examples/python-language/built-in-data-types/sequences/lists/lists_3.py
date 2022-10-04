#!/usr/bin/env python3

a = list('abcdef')      # Создание списка из десяти элементов через вызов функции на основе строки
print(a)                 # Выведет: ['a', 'b', 'c', 'd', 'e', 'f']

b = 'b'                  # Строка из одного символа
print(b in a)            # Выведет: True
print(b not in a)        # Выведет: False

c = a + list('ghijkl')   # Конкатенация списков
print(c)                 # Выведет: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

print(len(a))            # Выведет: 6
print(min(a))            # Выведет: a
print(max(a))            # Выведет: f

print(a.index('d'))      # Выведет: 3
# print(a.index('g'))    # ValueError: 'g' is not in list
print(a.count('d'))      # Выведет: 1

d = a * 3                # Повторение всех элементов списка три раза
# d = a * 2.5            # TypeError: can't multiply sequence by non-int of type 'float'
print(d)                 # Выведет: ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']

d = 3 * a                # При повторении последовательности порядок операндов на результат не влияет
print(d)                 # Выведет: ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']

a = [                    # Инициализация списка через литерал
    list('abc'),         # Инициализация вложенного списка через функцию
    list('012'),         # Инициализация вложенного списка через функцию
]
print(a)                 # Выведет: [['a', 'b', 'c'], ['0', '1', '2']]

b = a * 3                # Трёхкратное Повторение списка создаёт новые ссылки на списки внутри списка
print(b)                 # Выведет: [['a', 'b', 'c'], ['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2']]

del b[0][2], b[1][2]     # Удаление последнего элемента нулевого списка и последнего элемента первого списка
print(b)                 # [['a', 'b'], ['0', '1'], ['a', 'b'], ['0', '1'], ['a', 'b'], ['0', '1']]