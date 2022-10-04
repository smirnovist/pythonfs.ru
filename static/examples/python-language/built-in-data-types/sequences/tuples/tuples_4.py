#!/usr/bin/env python3

a, b = 'one', 'two'             # Распаковка кортежа: две переменные связываются с двумя элементами кортежа
print(a, b, sep=', ')           # Выведет: one, two

# a, b = 'one', 'two', 'three'  # ValueError: too many values to unpack (expected 2)
# a, b = 'one',                 # ValueError: not enough values to unpack (expected 2, got 1)

c = a, b = 'one', 'two'         # При распаковке связываются элементы кортежей, объявленных слева и справа от оператора присваивания
print(a, b, c, sep=', ')        # Выведет: one, two, ('one', 'two')

a, b = '!?'                     # Элементы кортежа, объявленного слева, связываются с элементами строки, объявленной справа
print(a, b, sep=', ')           # Выведет: !, ?

a, b = ['one', 'two']           # Элементы кортежа, объявленного слева, связываются с элементами списка, объявленного справа
print(a, b, sep=', ')           # Выведет: one, two


def test(sequence):
    """ Функция возвращает ссылку на кортеж, состоящий из первых трёх элементов последовательности """
    return sequence[0], sequence[1], sequence[2]


a, b, c = test(['one', 'two', 'three', 'four', 'five', 'six'])  # Вызов функции с аргументом — списком из шести строк
print(a, b, c, sep=', ')                                        # Выведет: one, two, three

*a, b, c = 'one', 'two', 'three', 'four', 'five', 'six'         # Расширенный синтаксис: первая переменная будет списком
print(a, b, c, sep=', ')                                        # Выведет: ['one', 'two', 'three', 'four'], five, six

a, *b, c = 'one', 'two', 'three', 'four', 'five', 'six'         # Расширенный синтаксис: вторая переменная будет списком
print(a, b, c, sep=', ')                                        # Выведет: one, ['two', 'three', 'four', 'five'], six

a, b, *c = 'one', 'two', 'three', 'four', 'five', 'six'         # Расширенный синтаксис: третья переменная будет списком
print(a, b, c, sep=', ')                                        # Выведет: one, two, ['three', 'four', 'five', 'six']

# *a, *b, *c = 'one', 'two', 'three', 'four', 'five', 'six'     # SyntaxError: two starred expressions in assignment

*a, b, c = 'one', 'two'           # Элементов кортежа слева (переменных) на один больше, чем элементов кортежа справа
print(a, b, c, sep=', ')          # Выведет: [], one, two

*a, b, c = 'one', 'two', 'three'  # Элементов кортежа слева (переменных) столько же, сколько элементов кортежа справа
print(a, b, c, sep=', ')          # Выведет: ['one'], two, three

# *a, b, c = 'one',               # ValueError: not enough values to unpack (expected at least 2, got 1)

a, b = False, True                # Распаковка кортежа
print(a, b, sep=', ')             # Выведет: False, True

a, b = b, a                       # У переменных a и b взаимно меняются ссылки на объекты
print(a, b, sep=', ')             # Выведет: True, False

a = 'abcdef'                      # Последовательность: строка
b = tuple(a)                      # Последовательность: кортеж
c = list(a)                       # Последовательность: список

print(a, *a, sep=', ')            # Выведет: abcdef, a, b, c, d, e, f
print(b, *c, sep=', ')            # Выведет: ('a', 'b', 'c', 'd', 'e', 'f'), a, b, c, d, e, f
print(c, *c, sep=', ')            # Выведет: ['a', 'b', 'c', 'd', 'e', 'f'], a, b, c, d, e, f
