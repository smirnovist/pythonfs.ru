#!/usr/bin/env python3

# Ввод данных в программу
a = input('Введите целое число: ')  # Вводим целое число. Функция возвращает ссылку на объект строки
a = int(a)                          # Преобразуем объект строки в объект целого числа

# Условная конструкция
if a == 1:
    print('a равно 1')
else:
    print('a не равно 1')

# Условное выражение
print('a равно 1') if a == 1 else print('a не равно 1')
# Условное выражение можно прочитать так:
# Вывести 'a равно 1', если выражение a == 1 истинно. В противном случае вывести 'a не равно 1'