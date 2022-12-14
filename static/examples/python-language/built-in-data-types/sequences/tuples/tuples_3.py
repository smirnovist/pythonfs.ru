#!/usr/bin/env python3

a = tuple('abcdef')                           # Создание кортежа через вызов функции на основе итерируемого объекта (строки)
print(a)                                      # Выведет: ('a', 'b', 'c', 'd', 'e', 'f')

print(a[0])                                   # Выведет: a
print(a[1])                                   # Выведет: b
print(a[2])                                   # Выведет: c
print(a[3])                                   # Выведет: d
print(a[4])                                   # Выведет: e
print(a[5])                                   # Выведет: f

print(a[-6])                                  # Выведет: a
print(a[-5])                                  # Выведет: b
print(a[-4])                                  # Выведет: c
print(a[-3])                                  # Выведет: d
print(a[-2])                                  # Выведет: e
print(a[-1])                                  # Выведет: f

print(a[len(a) - 6])                          # Выведет: a
print(a[len(a) - 5])                          # Выведет: b
print(a[len(a) - 4])                          # Выведет: c
print(a[len(a) - 3])                          # Выведет: d
print(a[len(a) - 2])                          # Выведет: e
print(a[len(a) - 1])                          # Выведет: f

a = (                                         # Создание кортежа из двух элементов через литерал
    ('a', 'b', 'c'),                          # Создание вложенного кортежа из трёх элементов через литерал
    ('d', 'e', 'f')                           # Создание вложенного кортежа из трёх элементов через литерал
)

print(a[0][0])                                # Выведет: a
print(a[0][1])                                # Выведет: b
print(a[0][2])                                # Выведет: c
print(a[1][0])                                # Выведет: d
print(a[1][1])                                # Выведет: e
print(a[1][2])                                # Выведет: f

print(a[-2][-3])                              # Выведет: a
print(a[-2][-2])                              # Выведет: b
print(a[-2][-1])                              # Выведет: c
print(a[-1][-3])                              # Выведет: d
print(a[-1][-2])                              # Выведет: e
print(a[-1][-1])                              # Выведет: f

print(a[len(a) - 2][len(a[len(a) - 1]) - 3])  # Выведет: a
print(a[len(a) - 2][len(a[len(a) - 1]) - 2])  # Выведет: b
print(a[len(a) - 2][len(a[len(a) - 1]) - 1])  # Выведет: c
print(a[len(a) - 1][len(a[len(a) - 1]) - 3])  # Выведет: d
print(a[len(a) - 1][len(a[len(a) - 1]) - 2])  # Выведет: e
print(a[len(a) - 1][len(a[len(a) - 1]) - 1])  # Выведет: f

a = ('a', 'b')                                # Создание кортежа из двух элементов через литерал
i = int(input('Введите целое число: '))       # Приглашение ввода целого числа
print(a[0 if i < 10 else 1])                  # Выведет: a или b в зависимости от того, будет i меньше 10 или нет

# Индексы элементов могут быт указаны булевыми константами
print(a[False])                               # Выведет: a
print(a[True])                                # Выведет: b

# Индексы элементов обязательно должны быть указаны целыми числами (включая булевы константы)
# print(a[0.0])                               # TypeError: tuple indices must be integers or slices, not float
