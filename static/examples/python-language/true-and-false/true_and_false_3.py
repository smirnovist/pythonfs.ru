#!/usr/bin/env python3

# Объявление переменных
a = 'строка 1'
b = 'строка 2'

# В f-строку можно включать вызов функции
print(f'id(a) = {id(a)}')
print(f'id(b) = {id(b)}')

# Пример оператора is
print(a is b)               # Выведет: False
print(id(a) == id(b))       # Выведет: False
print(id(a) is id(b))       # Выведет: False

# Пример оператора is not
print(a is not b)           # Выведет: True
print(id(a) != id(b))       # Выведет: True
print(id(a) is not id(b))   # Выведет: True

# Операторы is и is not с литералами
print(a is 'строка 3')      # Выведет: SyntaxWarning: "is" with a literal. Did you mean "=="?
print(a is not 'строка 3')  # Выведет: SyntaxWarning: "is not" with a literal. Did you mean "!="?
