#!/usr/bin/env python3

def greet(first, second):
    """ Функция выводит приветствие по имени """
    print(f'{first}, {second}!')


# Объявление глобальных переменных
greeting = 'Привет'
name = 'друг'

# Вызов функции
greet(first=greeting, second=name)
