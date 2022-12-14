#!/usr/bin/env python3

a = tuple('0123456789')     # Создание кортежа из десяти элементов через вызов функции на основе строки
print(a, len(a), sep=', ')  # Выведет: ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 10

# Доступ к элементам при отсчёте с начала последовательности
i = 0
while i < len(a):
    print(f'a[{i}] = {a[i]}, {type(a[i])}')
    i += 1
# Выведет:
# a[0] = 0, <class 'str'>
# a[1] = 1, <class 'str'>
# a[2] = 2, <class 'str'>
# a[3] = 3, <class 'str'>
# a[4] = 4, <class 'str'>
# a[5] = 5, <class 'str'>
# a[6] = 6, <class 'str'>
# a[7] = 7, <class 'str'>
# a[8] = 8, <class 'str'>
# a[9] = 9, <class 'str'>

# Для изменяемых последовательностей срез из всех элементов возвращает поверхностную копию последовательности (аналогичный вызову метода copy())
# Для неизменяемых последовательностей срез из всех элементов идентичен исходной последовательности
s = a[0:len(a)]                      # Через двоеточие указываются значение, равное индексу начального элемента и длина последовательности
print(s, len(s), s is a, sep=', ')   # Выведет: ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 10, True
s = a[0:]                            # Если указать только значение, равное индексу начального элемента, будет возвращен срез до конца последователньсти
print(s, len(s), s is a, sep=', ')   # Выведет: ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 10, True
s = a[:]                             # Для взятия срез из всех элементов, можно не указывать начальное и конечное смещение
print(s, len(s), s is a, sep=', ')   # Выведет: ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 10, True

# Срезы всегда относятся к тому же типу данных, что и исходная последовательность
s = a[:len(a) // 2]                  # Взятие среза, включающего первую половину последовательности
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1', '2', '3', '4'), 5, <class 'tuple'>
s = a[len(a) // 2:]                  # Взятие среза, включающего вторую половину последовательности
print(s, len(s), type(s), sep=', ')  # Выведет: ('5', '6', '7', '8', '9'), 5, <class 'tuple'>

# Границы срезов указаны положительными числами
s = a[0:2]                           # Взятие среза, состоящего из двух элементов: со смещением, равным 0 и 1
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1'), 2, <class 'tuple'>
s = a[2:4]                           # Взятие среза, состоящего из двух элементов: со смещением, равным 2 и 3
print(s, len(s), type(s), sep=', ')  # Выведет: ('2', '3'), 2, <class 'tuple'>
s = a[4:6]                           # Взятие среза, состоящего из двух элементов: со смещением, равным 2 и 3
print(s, len(s), type(s), sep=', ')  # Выведет: ('4', '5'), 2, <class 'tuple'>
s = a[6:7]                           # Взятие среза, состоящего из одного элемента: со смещением, равным 6
print(s, len(s), type(s), sep=', ')  # Выведет: ('6',), 1, <class 'tuple'>

# Пустая последовательность
s = a[7:7]                           # Пустая последовательность — начало и конец среза равны, при любом шаге
print(s, len(s), type(s), sep=', ')  # Выведет: (), 0, <class 'tuple'>
s = a[7:6]                           # Пустая последовательность — начало больше, чем конец среза, при положительном шаге
print(s, len(s), type(s), sep=', ')  # Выведет: (), 0, <class 'tuple'>

# Доступ к элементам при отсчёте с конца последовательности
i = -len(a)
while i <= -1:
    print(f'a[{i}] = {a[i]}, {type(a[i])}')
    i += 1
# Выведет:
# a[-10] = 0, <class 'str'>
# a[-9] = 1, <class 'str'>
# a[-8] = 2, <class 'str'>
# a[-7] = 3, <class 'str'>
# a[-6] = 4, <class 'str'>
# a[-5] = 5, <class 'str'>
# a[-4] = 6, <class 'str'>
# a[-3] = 7, <class 'str'>
# a[-2] = 8, <class 'str'>
# a[-1] = 9, <class 'str'>

# Границы срезов указаны отрицательными числами
s = a[-10: -8]                       # Взятие среза, состоящего из двух элементов: со смещением, равным 0 и 1
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1'), 2, <class 'tuple'>
s = a[-8: -6]                        # Взятие среза, состоящего из двух элементов: со смещением, равным 2 и 3
print(s, len(s), type(s), sep=', ')  # Выведет: ('2', '3'), 2, <class 'tuple'>
s = a[-6:-4]                         # Взятие среза, состоящего из двух элементов: со смещением, равным 4 и 5
print(s, len(s), type(s), sep=', ')  # Выведет: ('4', '5'), 2, <class 'tuple'>
s = a[-4:-4]                         # Пустая последовательность — начало и конец среза равны, при любом шаге
print(s, len(s), type(s), sep=', ')  # Выведет: (), 0, <class 'tuple'>
s = a[-20:-8]                        # Взятие среза, состоящего из двух элементов: со смещением, равным 0 и 1
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1'), 2, <class 'tuple'>

# Прямой порядок среза — положительный шаг
s = a[::]                            # Прямой порядок среза — положительный шаг равен 1
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 10, <class 'tuple'>
s = a[::1]                           # Прямой порядок среза — положительный шаг равен 1
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), 10, <class 'tuple'>
s = a[::2]                           # Прямой порядок среза — положительный шаг равен 2
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '2', '4', '6', '8'), 5, <class 'tuple'>
s = a[::3]                           # Прямой порядок среза — положительный шаг равен 3
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '3', '6', '9'), 4, <class 'tuple'>

# Обратный порядок среза — отрицательный шаг
s = a[::-1]                          # Обратный порядок среза — отрицательный шаг равен -1
print(s, len(s), type(s), sep=', ')  # Выведет: ('9', '8', '7', '6', '5', '4', '3', '2', '1', '0'), 10, <class 'tuple'>
s = a[::-2]                          # Обратный порядок среза — отрицательный шаг равен -2
print(s, len(s), type(s), sep=', ')  # Выведет: ('9', '7', '5', '3', '1'), 5, <class 'tuple'>
s = a[::-3]                          # Обратный порядок среза — отрицательный шаг равен -3
print(s, len(s), type(s), sep=', ')  # Выведет: ('9', '6', '3', '0'), 4, <class 'tuple'>

# Комбинации положительных и отрицательных чисел для указания границ срезов
# Неважно, какой знак имеют числа, обозначающие границы. Важно, чтобы учитывался шаг — положительный или отрицательный
s = a[0:7:2]                         # Положительные числа для указания границ,, положительный шаг
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '2', '4', '6'), 4, <class 'tuple'>
s = a[0:7:-2]                        # Взятие среза с началом меньше, чем конец, при отрицательном шаге возвращает пустой срез
print(s, len(s), type(s), sep=', ')  # Выведет: (), 0, <class 'tuple'>
s = a[6:-11:-2]                      # Комбинация отрицательного и положительного чисел для указания границ, отрицательный шаг
print(s, len(s), type(s), sep=', ')  # Выведет: ('6', '4', '2', '0'), 4, <class 'tuple'>
s = a[9:-11:-3]                      # Комбинация положительного и отрицательного чисел для указания границ, отрицательный шаг
print(s, len(s), type(s), sep=', ')  # Выведет: ('9', '6', '3', '0'), 4, <class 'tuple'>
s = a[-1:-11:-3]                     # Отрицательные числа для указания границ, отрицательный шаг
print(s, len(s), type(s), sep=', ')  # Выведет: ('9', '6', '3', '0'), 4, <class 'tuple'>

# Границы среза и шаг обязательно должны быть указаны целыми числами (включая булевы константы)
s = a[False:2:True]
print(s, len(s), type(s), sep=', ')  # Выведет: ('0', '1'), 2, <class 'tuple'>
# s = a[0.0::]                       # TypeError: slice indices must be integers or None or have an __index__ method
# s = a[::1.0]                       # TypeError: slice indices must be integers or None or have an __index__ method

# Шаг не может быть равен нулю
# s = a[::0]                         # ValueError: slice step cannot be zero

# Прохождение по срезу в цикле
for e in a[-1:-11:-3]:               # Получение доступа к элементам среза
    print(e)
# Выведет:
# 9
# 6
# 3
# 0

for i, e in enumerate(a[-1:-11:-3]):  # Получение доступа к счётчику и элементам среза через функцию enumerate()
    print(i, e, sep=', ')
# Выведет:
# 0, 9
# 1, 6
# 2, 3
# 3, 0

t = tuple(enumerate(a[-1:-11:-3]))    # Преобразование объекта enumerate в кортеж
print(t)                              # Выведет: ((0, '9'), (1, '6'), (2, '3'), (3, '0'))

# Срез среза — работает, но практического смысла в этом нет
s = a[::2][::2]                       # Выражение a[::2][::2] вернёт то же, что срез a[::4]
print(s, len(s), type(s), sep=', ')   # Выведет: ('0', '4', '8'), 3, <class 'tuple'>

s1 = a[::2]                           # Взятие среза с положительным шагом, равным 2
for i, e in enumerate(s1):
    print(i, e, sep=', ')
# Выведет:
# 0, 0
# 1, 2
# 2, 4
# 3, 6
# 4, 8

s2 = s1[::2]                          # Взятие среза от кортежа, полученного в результате предыдущего взятия среза
for i, e in enumerate(s2):
    print(i, e, sep=', ')
# Выведет:
# 0, 0
# 1, 4
# 2, 8
