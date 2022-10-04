#!/usr/bin/env python3

a = list('012345')
a[:] = list('abc')
# print(id(a), id(b), sep=', ')
print(a)