#!/usr/bin/env python3

a = 1     # Объявление переменной
del a     # Удаление переменной
print(a)  # Здесь ошибка: попытка обратиться к несуществующей переменной

"""
Интерпретатор выведет следующие строки:
Traceback (most recent call last):
  File "./variables4.py", line 5, in <module>
    print(a)
NameError: name 'a' is not defined
"""
