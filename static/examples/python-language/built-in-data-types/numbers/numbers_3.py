#!/usr/bin/env python3

a = 1
b = 2
print(a, bin(a), sep=' = ')  # Выведет: 1 = 0b1
print(b, bin(b), sep=' = ')  # Выведет: 2 = 0b10

c = a | b                    # Побитовое ИЛИ
print(c, bin(c), sep=' = ')  # Выведет: 3 = 0b11

c = a ^ b                    # Побитовое исключающее ИЛИ
print(c, bin(c), sep=' = ')  # Выведет: 3 = 0b11

c = a & b                    # Побитовое И
print(c, bin(c), sep=' = ')  # Выведет: 0 = 0b0

c = a << 1                   # Арифметический битовый сдвиг влево
print(c, bin(c), sep=' = ')  # Выведет: 2 = 0b10

c = a >> 1                   # Арифметический битовый сдвиг вправо
print(c, bin(c), sep=' = ')  # Выведет: 0 = 0b0

c = ~a                       # Побитовое НЕ
print(c, bin(c), sep=' = ')  # Выведет: -2 = -0b10
