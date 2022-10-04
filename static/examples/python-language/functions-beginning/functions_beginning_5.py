#!/usr/bin/env python3

# Аргументы name и surname могут быть как позиционными, так и именованными
# Аргументы message и mark должны быть только именованными
def greet(name, surname, *, message='Привет', mark='!'):
    """ Функция выводит приветствие по имени """
    # Переменные, объявленные внутри функции — локальные
    output = f'{message}, {name} {surname}{mark}'
    print(output)


# Объявление глобальных переменных
name = input('Назовите ваше имя: ')         # Приглашение для ввода данных
surname = input('Назовите вашу фамилию: ')  # Приглашение для ввода данных
# Вызов функции
greet(name, surname, message='Здравствуй')  # Первые два аргумента — позиционные, message — именованный
greet(name=name, surname=surname, message='Здравствуй')  # Именованный способ передачи аргументов
# greet(name, surname, 'Здравствуй')  # TypeError: greet() takes 2 positional arguments but 3 were given
