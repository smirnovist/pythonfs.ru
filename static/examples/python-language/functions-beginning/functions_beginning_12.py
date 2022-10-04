#!/usr/bin/env python3

def concatenate(a, b):           # Вернёт: результат сложения или объединения (конкатенации) объектов
    return a + b


def divide_with_reminder(a, b):  # Вернёт: целое частное и остаток от деления
    quotient = a // b
    remainder = a % b
    return (quotient, remainder)


def test1(a):                    # Вернёт: три ссылки на один объект
    print(id(a))
    return a, a, a


def test2(a):                    # Вернёт: None
    return
    print(id(a))                 # Эта инструкция никогда не будет выполнена


def test3(a):                    # Вернёт: None
    print(id(a))                 # Выведет: целое число — идентификатор объекта a
    return None


def test4(a):                    # Вернёт: None
    print(id(a))                 # Выведет: целое число — идентификатор объекта a
    return


def test5(a):                    # Вернёт: None
    print(id(a))                 # Выведет: целое число — идентификатор объекта a


result = concatenate(1, 2)
print(result)                         # Выведет: 3

result = concatenate('гипер', 'текст')
print(result)                         # Выведет: гипертекст

quotient, remainder = divide_with_reminder(7, 3)
print(quotient, remainder, sep=', ')  # Выедет: 2, 1

a = 'строка'
print(id(a))

b, c, d = test1(a)
print(id(b), id(c), id(d), sep=', ')  # Выведет: три раза тот же идентификатор, что у переменной `a`, объявленной на строке 46
print(b, c, d, sep=', ')              # Выведет: строка, строка, строка

print(test2(a))                       # Выведет: None
print(test3(a))                       # Выведет: None
print(test4(a))                       # Выведет: None
print(test4(a))                       # Выведет: None
