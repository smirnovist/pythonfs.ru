#!/usr/bin/env python3

a = list('012345')  # Задаём список из шести элементов
print(a)            # Выведет: ['0', '1', '2', '3', '4', '5']

for i, e in enumerate(a):
    print(f"index = {i}, element = '{e}', a[{i}] = '{a[i]}'")
# Выведет:
# index = 0, element = '0', a[0] = '0'
# index = 1, element = '1', a[1] = '1'
# index = 2, element = '2', a[2] = '2'
# index = 3, element = '3', a[3] = '3'
# index = 4, element = '4', a[4] = '4'
# index = 5, element = '5', a[5] = '5'

print(a)            # Выведет: ['0', '1', '2', '3', '4', '5']

for i, e in enumerate(a):
    print(f"before del: index = {i}, element = '{e}', a[{i}] = '{a[i]}'")  # Счётчик итератора обновляется после каждого изменения списка
    del a[i]                                                               # Удаление элемента из списка по индексу
    print(f"after  del: index = {i}, element = '{e}', a[{i}] = '{a[i]}'")  # После удаления a[i] содержит ссылку на другой объект
# Выведет:
# before del: index = 0, element = '0', a[0] = '0'
# after  del: index = 0, element = '0', a[0] = '1'
# before del: index = 1, element = '2', a[1] = '2'
# after  del: index = 1, element = '2', a[1] = '3'
# before del: index = 2, element = '4', a[2] = '4'
# after  del: index = 2, element = '4', a[2] = '5'

print(a)            # Выведет: ['1', '3', '5']

a = list('012345')  # Заново задаём список
print(a)            # Выведет: ['0', '1', '2', '3', '4', '5']

for i, e in enumerate(a):
    print(f"before del and insert: index = {i}, element = '{e}', a[{i}] = '{a[i]}'")
    del a[i]
    a.insert(i, e)
    print(f"after  del and insert: index = {i}, element = '{e}', a[{i}] = '{a[i]}'")
# Выведет:
# before del and insert: index = 0, element = '0', a[0] = '0'
# after  del and insert: index = 0, element = '0', a[0] = '0'
# before del and insert: index = 1, element = '1', a[1] = '1'
# after  del and insert: index = 1, element = '1', a[1] = '1'
# before del and insert: index = 2, element = '2', a[2] = '2'
# after  del and insert: index = 2, element = '2', a[2] = '2'
# before del and insert: index = 3, element = '3', a[3] = '3'
# after  del and insert: index = 3, element = '3', a[3] = '3'
# before del and insert: index = 4, element = '4', a[4] = '4'
# after  del and insert: index = 4, element = '4', a[4] = '4'
# before del and insert: index = 5, element = '5', a[5] = '5'
# after  del and insert: index = 5, element = '5', a[5] = '5'

print(a)            # Выведет: ['0', '1', '2', '3', '4', '5']
