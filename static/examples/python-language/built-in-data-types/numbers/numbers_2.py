#!/usr/bin/env python3

int_number = -512             # Инициализируем отрицательное целое число, заданное через литерал в десятичной системе счисления
bin_string = bin(int_number)  # Преобразуем к строке, представляющей число в двоичной системе счисления с префиксом '0b'
oct_string = oct(int_number)  # Преобразуем к строке, представляющей число в восьмеричной системе счисления с префиксом '0o'
hex_string = hex(int_number)  # Преобразуем к строке, представляющей число в шестнадцатеричной системе счисления с префиксом '0x'

print(bin_string)             # Выведет: -0b1000000000
print(oct_string)             # Выведет: -0o1000
print(hex_string)             # Выведет: -0x200

int_number = -0b1000000000    # Инициализируем отрицательное целое число, заданное через литерал в двоичной системе счисления
bin_string = bin(int_number)  # Преобразуем к строке, представляющей число в двоичной системе счисления с префиксом '0b'
oct_string = oct(int_number)  # Преобразуем к строке, представляющей число в восьмеричной системе счисления с префиксом '0o'
hex_string = hex(int_number)  # Преобразуем к строке, представляющей число в шестнадцатеричной системе счисления с префиксом '0x'

print(bin_string)             # Выведет: -0b1000000000
print(oct_string)             # Выведет: -0o1000
print(hex_string)             # Выведет: -0x200
