#!/usr/bin/env python3

import decimal          # Импорт модуля decimal стандартной библиотеки
import fractions        # Импорт модуля fractions стандартной библиотеки

a = .07                 # Объявление числа с плавающей точкой через литерал c нулевой целой частью и ведущей точкой
print(a)                # Выведет: 0.07

a = 010_000_000.001     # Объявление числа с плавающей точкой через литерал c ведущим нулём и символом подчёркивания
print(a)                # Выведет: 10000000.001

a = float()             # Вызов без аргументов
print(a)                # Выведет: 0.0

a = float(True)         # Вызов с одним аргументом: передача числа типа bool
print(a)                # Выведет: 1.0

b = 3+10j               # Инициализация комплексного числа с ненулевой действительной частью
# a = float(b)          # Нельзя получить число с плавающей точкой на основе комплексного числа. TypeError: can't convert complex to float
print(type(b.real))     # Действительная часть комплексного числа является числом с плавающей точкой. Выведет: <class 'float'>
print(b.real)           # Выведет: 3.0
print(type(b.imag))     # Мнимая часть комплексного числа является числом с плавающей точкой. Выведет: <class 'float'>
print(b.imag)           # Выведет: 10.0

a = float(' -0128.05')  # Вызов с одним аргументом: передача строки с ведущим нулём, содержащей представление числа
print(a)                # Выведет: -128.05

a = float('-InFiNiTy')  # Вызов с одним аргументом: передача строки с буквами в верхнем и нижнем регистрах, представляющей отрицательную бесконечность
print(type(a))          # Выведет: <class 'float'>
print(a)                # Выведет: -inf
print(a + 100.5)        # Выведет: -inf
print(a - 100.5)        # Выведет: -inf
print(a * 100.5)        # Выведет: -inf
print(a / 100.5)        # Выведет: -inf
print(a + a)            # Выведет: -inf
print(a - a)            # Выведет: nan
print(a * a)            # Выведет: inf
print(a / a)            # Выведет: nan

a = float(' nan ')      # Вызов с одним аргументом: передача строки, представляющей 'не число'
print(type(a))          # Выведет: <class 'float'>
print(a)                # Выведет: nan
print(a + 100.5)        # Выведет: nan
print(a - 100.5)        # Выведет: nan
print(a * 100.5)        # Выведет: nan
print(a / 100.5)        # Выведет: nan
print(a + a)            # Выведет: nan
print(a - a)            # Выведет: nan
print(a * a)            # Выведет: nan
print(a / a)            # Выведет: nan

b = decimal.Decimal(128.123456789)  # Инициализация числа типа decimal.Decimal
print(b)                            # Выведет: 128.1234567889999880208051763474941253662109375
a = float(b)                        # Вызов с одним аргументом: передача числа типа decimal.Decimal
print(a)                            # Выведет: 128.123456789

b = fractions.Fraction(10, 6)       # Инициализация числа типа fractions.Fraction
print(b)                            # Выведет: 5/3
a = float(b)                        # Вызов с одним аргументом: передача числа типа fractions.Fraction
print(a)                            # Выведет: 1.6666666666666667

