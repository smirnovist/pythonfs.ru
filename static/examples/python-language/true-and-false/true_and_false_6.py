#!/usr/bin/env python3

print(not True)             # Выведет: False
print(not False)            # Выведет: True

print(not -1.0)             # Выведет: False
print(not 0.0)              # Выведет: True

print(not 'строка')         # Выведет: False
print(not '')               # Выведет: True


def plus(x, y):
    return x + y


print(not plus(1.1, 2.2))   # Выведет: False
print(not plus(-1.1, 1.1))  # Выведет: True

print(not not 0 == 1)       # Выведет: False
print(not not 0 + 1)        # Выведет: True
