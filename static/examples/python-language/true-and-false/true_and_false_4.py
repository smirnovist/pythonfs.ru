#!/usr/bin/env python3

print(1 - 1 and 2 + 2)             # Выедет: 0
print(bool(1 - 1))                 # Выведет: False

print(1 + 2 and 3 + 4)             # Выведет: 7
print(bool(1 + 2))                 # Выведет: True


def minus(x, y):
    return x - y


def plus(x, y):
    return x + y


print(minus(1, 1) and plus(2, 2))  # Выведет: 0
print(bool(minus(1, 1)))           # Выведет: False

print(plus(1, 2) and plus(3, 4))   # Выведет: 7
print(bool(plus(1, 2)))            # Выведет: True
