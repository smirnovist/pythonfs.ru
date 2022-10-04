#!/usr/bin/env python3

# Попытка вызова функции до её объявления
# hello()  # NameError: name 'hello' is not defined


# Объявление функции без параметров
def hello():
    print('Привет')


# Вызов функции hello()
hello()  # Выведет: Привет


# Повторное объявление функции с параметром name
def hello(name):
    print(f'Привет, {name}')


hello('друг')    # Выведет: Привет, друг
del hello        # Так же как переменную, функцию можно удалить
# hello('друг')  # NameError: name 'hello' is not defined
