#!/usr/bin/env python3

# Аргументы name и surname должны быть только позиционными
# Аргументы message и mark могут быть позиционными и именованными
def greet(name, surname, /, message='Привет', mark='!',):
    """ Функция выводит приветствие по имени """
    # Переменные, объявленные внутри функции — локальные
    output = f'{message}, {name} {surname}{mark}'
    print(output)


# Объявление глобальных переменных
name = input('Назовите ваше имя: ')         # Приглашение для ввода данных
surname = input('Назовите вашу фамилию: ')  # Приглашение для ввода данных
# Вызов функции
greet(name, surname)
greet(name, surname, 'Здравствуй')
greet(name, surname, message='Здравствуй')
# greet(name, surname=surname, message='Здравствуй')  # TypeError: greet() got some positional-only arguments passed as keyword arguments: 'surname'
