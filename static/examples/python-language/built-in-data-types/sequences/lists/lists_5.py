#!/usr/bin/env python3

def test(element, data=[]):          # При первом вызове функции создаётся пустой список data и хранится в памяти
    data.append(element)             # При каждом вызове функции в список data добавляется новый элемент
    print(id(data), data, sep=', ')  # Выведет один и тот же идентификатор списка data при каждом вызове функции


print(type(test))                    # Выведет: <class 'function'>
test('a')                            # Выведет: 140580417587840, ['a']
test('b')                            # Выведет: 140580417587840, ['a', 'b']
test('c')                            # Выведет: 140580417587840, ['a', 'b', 'c']


def test2(element, data=([],)):      # При первом вызове функции создаётся кортеж data и хранится в памяти
    data[0].append(element)          # При каждом вызове функции в нулевой элемент кортежа data добавляется новый элемент
    print(id(data), data, sep=', ')  # Выведет один и тот же идентификатор кортежа data при каждом вызове функции


print(type(test2))                   # Выведет: <class 'function'>
test2('a')                           # Выведет: 140580417075712, (['a'],)
test2('b')                           # Выведет: 140580417075712, (['a', 'b'],)
test2('c')                           # Выведет: 140580417075712, (['a', 'b', 'c'],)


def test3(element, data=[]):         # При первом вызове вызова функции создаётся пустой список data и хранится в памяти
    data.append(element)             # При каждом вызове функции в список data добавляется новый элемент
    return data                      # Функция ничего не выводит, а возвращает ссылку на список data


print(type(test3))                   # Выведет: <class 'function'>
a = test3('a')
print(id(a), a, sep=', ')            # Выведет: 140580416793344, ['a']
a.append('b')
print(id(a), a, sep=', ')            # Выведет: 140580416793344, ['a', 'b']
test3('c')
print(id(a), a, sep=', ')            # Выведет: 140580416793344, ['a', 'b', 'c']


def test4(element, data=([],)):      # При первом вызове функции создаётся кортеж data и хранится в памяти
    data[0].append(element)          # При каждом вызове функции в нулевой элемент кортежа data добавляется новый элемент
    return data                      # Функция ничего не выводит, а возвращает ссылку на кортеж data


print(type(test4))                   # Выведет: <class 'function'>
a = test4('a')
print(id(a), a, sep=', ')            # Выведет: 140580417818336, (['a'],)
a[0].append('b')
print(id(a), a, sep=', ')            # Выведет: 140580417818336, (['a', 'b'],)
test4('c')
print(id(a), a, sep=', ')            # Выведет: 140580417818336, (['a', 'b', 'c'],)
