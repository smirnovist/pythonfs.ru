#!/usr/bin/env python3

a = 'a', 'b', 'c', 'd', 'e'  # Объявляем коллекцию (в данном случае — последовательность — кортеж)

# Первый вариант: обращение к элементам коллекции напрямую
i = a[0]                     # Получаем первый элемент коллекции    (элемент с индексом 0)
print(i)                     # Выводим первый элемент коллекции     (элемент с индексом 0)
i = a[1]                     # Получаем второй элемент коллекции    (элемент с индексом 1)
print(i)                     # Выводим второй элемент коллекции     (элемент с индексом 1)
i = a[2]                     # Получаем третий элемент коллекции    (элемент с индексом 2)
print(i)                     # Выводим третий элемент коллекции     (элемент с индексом 2)
i = a[3]                     # Получаем четвёртый элемент коллекции (элемент с индексом 3)
print(i)                     # Выводим четвёртый элемент коллекции  (элемент с индексом 3)
i = a[4]                     # Получаем пятый элемент коллекции     (элемент с индексом 4)
print(i)                     # Выводим пятый элемент коллекции      (элемент с индексом 4)
print('Обработка завершена')

# Второй вариант: цикл while без итератора
k = 0                        # Объявляем вспомогательную переменную для обращения к элементам коллекции
# Начало цикла
while k < len(a):            # Объявляем цикл. Количество итераций цикла равно количеству элементов коллекции
    i = a[k]                 # Получаем ссылку на текущий элемент коллекции
    print(i)                 # Выводим текущий элемент коллекции
    k += 1                   # Увеличиваем вспомогательную переменную на единицу
else:                        # Эта инструкция будет вызвана,
    print('Цикл завершён')   # когда интерпретатор пройдёт по всем элементы коллекции
# Выведет:
# a
# b
# c
# d
# e
# Цикл завершён
