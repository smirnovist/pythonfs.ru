#!/usr/bin/env python3

# Все аргументы должны быть только именованными
def greet(*, name, surname, message='Привет', mark='!'):
    """ Функция выводит приветствие по имени """
    # Переменные, объявленные внутри функции — локальные
    output = f'{message}, {name} {surname}{mark}'
    print(output)


# Объявление глобальных переменных
name = input('Назовите ваше имя: ')         # Приглашение для ввода данных
surname = input('Назовите вашу фамилию: ')  # Приглашение для ввода данных
# Вызов функции
greet(name=name, surname=surname, message='Здравствуй')  # Аргумент mark не указан, так как имеет значение по умолчанию
greet(name=name, surname=surname)             # Аргументы message и mark не указаны, так как оба имеют значения по умолчанию
greet(name=name, surname=surname, mark='.')   # Аргумент message не указан, так как имеет значение по умолчанию
greet(mark='.', surname=surname, name=name)   # Порядок именованных аргументов может быть произвольный, аргумент message не указан
# greet(name, surname, message='Здравствуй')  # TypeError: greet() takes 0 positional arguments but 2 positional arguments (and 1 keyword-only argument) were given