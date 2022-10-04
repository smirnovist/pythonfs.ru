#!/usr/bin/env python3

def greet(name, greeting):
    """ Функция выводит приветствие по имени """
    print(f'{greeting}, {name}!')


# Ввод данных в программу
name = input('Назовите ваше имя: ')
greeting = input('Укажите, как вас приветствовать: ')

# Вызов функции greet()
greet(name, greeting)                # Позиционный способ передачи аргументов
greet(name=name, greeting=greeting)  # Именованный способ передачи аргументов
