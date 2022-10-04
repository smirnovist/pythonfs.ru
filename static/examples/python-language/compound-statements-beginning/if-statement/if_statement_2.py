#!/usr/bin/env python3

# Ввод данных в программу
a = input('Введите целое число: ')  # Вводим целое число. Функция возвращает ссылку на объект строки
a = int(a)                          # Преобразуем объект строки в объект целого числа

# Начало условной конструкции
if a > 0 and a < 2:                 # Проверка на соответствие первому условию
    print('a равно 1')              # Если первое условие выполнено, выводим строку и переходим в конец ветвления
elif a > 1 and a < 3:               # Если первое условие не выполнено, проверяем на соответствие второму условию
    print('a равно 2')              # Если второе условие выполнено, выводим строку и переходим в конец ветвления
elif a > 2 and a < 4:               # Если второе условие не выполнено, проверяем на соответствие третьему условию
    print('a равно 3')              # Если третье условие выполнено, выводим строку и переходим в конец ветвления
else:                               # Если ни одно условие не выполнено,
    print('a не равно 1, 2, 3')     # выводим строку и завершаем обработку
# Конец условной конструкции

# Продолжение программы
print(f'Это сообщение не зависит ни от каких условий: a = {a}')