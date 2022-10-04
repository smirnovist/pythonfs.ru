#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Литералы строк
s1 = 'строка в одинарных кавычках позволяет вставлять "двойные" кавычки внутри строки'
s2 = "строка в двойных кавычках позволяет вставлять 'одинарные' кавычки внутри строки"
s3 = '''одна или несколько строк в тройных одинарных кавычках позволяют вставлять 'одинарные' и "двойные" кавычки внутри строки'''
s4 = """одна или несколько строк в тройных двойных кавычках позволяют вставлять 'одинарные' и "двойные" кавычки внутри строки"""
print(s1, s2, s3, s4, sep='\n')
# Выведет:
# строка в одинарных кавычках позволяет вставлять "двойные" кавычки внутри строки
# строка в двойных кавычках позволяет вставлять 'одинарные' кавычки внутри строки
# одна или несколько строк в тройных одинарных кавычках позволяют вставлять 'одинарные' и "двойные" кавычки внутри строки
# одна или несколько строк в тройных двойных кавычках позволяют вставлять 'одинарные' и "двойные" кавычки внутри строки

# Экранирование символов при помощи символа \ (обратный слеш)
s5 = 'строка в одинарных кавычках позволяет вставлять экранированные \'одинарные\' и \"двойные\" кавычки внутри строки'
s6 = "строка в двойных кавычках позволяет вставлять экранированные \'одинарные\' и \"двойные\" кавычки внутри строки"
s7 = 'строка с экранированным \\ обратным слешем'
print(s5, s6, s7, sep='\n')
# Выведет:
# строка в одинарных кавычках позволяет вставлять экранированные 'одинарные' и "двойные" кавычки внутри строки
# строка в двойных кавычках позволяет вставлять экранированные 'одинарные' и "двойные" кавычки внутри строки
# строка с экранированным \ обратным слешем

# Перенос строки
s8 = 'строка с переводом \nна новую строку'
print(s8)
# Выведет:
# строка с переводом
# на новую строку

print(repr(s8))
# Выведет:
# 'строка с переводом \nна новую строку'

# Сырые (raw) строки без необходимости экранирования
s9 = r'сырая строка с переводом строки \n не переводится на новую строку'
print(s9)
# Выведет:
# сырая строка с переводом строки \n не переводится на новую строку

print(repr(s9))
# Выведет:
# 'сырая строка с переводом строки \\n не переводится на новую строку'

# Экранированные последовательности
ruble1 = '₽'                                # Если шрифт поддерживает категорию "Символы валют", будет отображён символ рубля
ruble2 = '\N{RUBLE SIGN}'                   # Управляющая последовательность с названием кодовой позиции в базе данных Юникода
ruble3 = '\u20BD'                           # Управляющая последовательность с 16-битным представлением кодовой позиции
ruble4 = '\U000020BD'                       # Управляющая последовательность с 32-битным представлением кодовой позиции
print(ruble1, ruble2, ruble3, ruble4)       # Выедет: ₽ ₽ ₽ ₽

ruble5 = '₽\N{RUBLE SIGN}\u20BD\U000020BD'  # Интерпретатор распознаёт управляющие последовательности, следующие друг за другом
print(ruble5)                               # Выведет: ₽₽₽₽

print(ord('\N{RUBLE SIGN}'))                # Выведет: 8381
print(chr(8381))                            # Выведет: ₽
print(hex(8381))                            # Выведет: 0x20bd

# Объединение (конкатенация) строк
s10 = 'начало и ' + 'продолжение ' + 'строки'
print(s10)
# Выведет:
# начало и продолжение строки

# Одна логическая строка соответствует одной физической строке
lorem_ipsum1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(lorem_ipsum1)
# Выведет:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# Одна логическая строка соответствует восьми физическим строкам — первый способ (рекомендуемый)
lorem_ipsum2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
               'sed do eiusmod tempor incididunt ut labore et dolore magna ' \
               'aliqua. Ut enim ad minim veniam, quis nostrud exercitation ' \
               'ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis ' \
               'aute irure dolor in reprehenderit in voluptate velit esse ' \
               'cillum dolore eu fugiat nulla pariatur. Excepteur sint ' \
               'occaecat cupidatat non proident, sunt in culpa qui officia ' \
               'deserunt mollit anim id est laborum.'
print(lorem_ipsum2)
# Выведет:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# Одна логическая строка соответствует восьми физическим строкам — второй способ (избыточный)
lorem_ipsum3 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' + \
               'sed do eiusmod tempor incididunt ut labore et dolore magna ' + \
               'aliqua. Ut enim ad minim veniam, quis nostrud exercitation ' + \
               'ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis ' + \
               'aute irure dolor in reprehenderit in voluptate velit esse ' + \
               'cillum dolore eu fugiat nulla pariatur. Excepteur sint ' + \
               'occaecat cupidatat non proident, sunt in culpa qui officia ' + \
               'deserunt mollit anim id est laborum.'
print(lorem_ipsum3)
# Выведет:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# Одна логическая строка соответствует восьми физическим строкам — третий способ (заключение в скобки и неявная конкатенация)
lorem_ipsum4 = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                'sed do eiusmod tempor incididunt ut labore et dolore magna '
                'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                'ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis '
                'aute irure dolor in reprehenderit in voluptate velit esse '
                'cillum dolore eu fugiat nulla pariatur. Excepteur sint '
                'occaecat cupidatat non proident, sunt in culpa qui officia '
                'deserunt mollit anim id est laborum.')
print(lorem_ipsum4)
# Выведет:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

print(lorem_ipsum1 is lorem_ipsum2 is lorem_ipsum3 is lorem_ipsum4)  # Выведет: True

# Строка с символами новой строки в тройных кавычках
lorem_ipsum5 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(lorem_ipsum5)
# Выведет:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam,
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident,
# sunt in culpa qui officia deserunt mollit anim id est laborum.

print(repr(lorem_ipsum5))
# Выведет:
# 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam,\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident,\nsunt in culpa qui officia deserunt mollit anim id est laborum.'
