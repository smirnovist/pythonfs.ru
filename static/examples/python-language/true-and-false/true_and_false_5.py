#!/usr/bin/env python3

print(1 - 1 or 2 + 2)             # Выедет: 4
print(bool(1 - 1))                # Выведет: False

print(1 + 2 or 3 + 4)             # Выведет: 3
print(bool(1 + 2))                # Выведет: True


def minus(x, y):
    return x - y


def plus(x, y):
    return x + y


print(minus(1, 1) or plus(2, 2))  # Выведет: 4
print(bool(minus(1, 1)))          # Выведет: False

print(plus(1, 2) or plus(3, 4))   # Выведет: 3
print(bool(plus(1, 2)))           # Выведет: True
