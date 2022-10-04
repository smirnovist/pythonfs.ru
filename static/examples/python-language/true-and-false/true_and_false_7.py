#!/usr/bin/env python3

a = 1
b = 2
c = 3
d = 4

if a < b and c < d:
    print('Условие выполнено')
else:
    print('Условие не выполнено')

if a < b or c < d:
    print('Условие выполнено')
else:
    print('Условие не выполнено')

if not a > b and not c > d:
    print('Условие выполнено')
else:
    print('Условие не выполнено')
