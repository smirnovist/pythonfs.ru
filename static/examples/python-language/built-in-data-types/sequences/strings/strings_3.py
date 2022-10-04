#!/usr/bin/env python3

s1 = str(1)
print(s1, repr(s1), sep=', ')    # Выведет: 1, '1'

s2 = str(1.1)
print(s2, repr(s2), sep=', ')    # Выведет: 1.1, '1.1'

s3 = str(True)
print(s3, repr(s3), sep=', ')    # Выведет: True, 'True'

s4 = str(None)
print(s4, repr(s4), sep=', ')    # Выведет: None, 'None'

s5 = str(NotImplemented)
print(s5, repr(s5), sep=', ')    # Выведет: NotImplemented, 'NotImplemented'

s6 = tuple('abc')
print(s6, repr(s6), sep=', ')    # Выведет: ('a', 'b', 'c'), ('a', 'b', 'c')

s7 = str(["a", "b", "c"])
print(s7, repr(s7), sep=', ')    # Выведет: ['a', 'b', 'c'], "['a', 'b', 'c']"

s8 = str(b'string')
print(s8, repr(s8), sep=', ')    # Выведет: b'string', "b'string'"

# Получаем объект типа str на основе объекта типа bytes без указания кодировки (аргумент encoding)
s9 = str(b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82')
print(s9, repr(s9), sep='\n')
# Выведет:
# b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# "b'\\xd0\\xbf\\xd1\\x80\\xd0\\xb8\\xd0\\xb2\\xd0\\xb5\\xd1\\x82'"

# Получаем объект типа str на основе объекта типа bytes с указанием кодировки (аргумент encoding)
s10 = str(b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82', 'utf-8')
print(s10, repr(s10), sep=', ')  # Выведет: привет, 'привет'

# Получаем объект типа bytes на основе объекта типа str
b1 = 'привет'.encode()
print(b1, repr(b1), sep='\n')
# Выведет:
# b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Получаем объект типа str на основе объекта типа bytes, что эквивалентно инструкции на строке 35
s11 = b1.decode()
print(s11, repr(s11), sep=', ')  # Выведет: привет, 'привет'

s12 = str(print)
print(s12, repr(s12), sep=', ')  # Выведет: <built-in function print>, '<built-in function print>'

s13 = str(int)
print(s13, repr(s13), sep=', ')  # Выведет: <class 'int'>, "<class 'int'>"
