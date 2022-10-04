#!/usr/bin/env python3

a = dict(a='b', c='d')
print(a)


b = dict(a, v='h')
print(b)

# c = dict(list('avf'), h='j', q='g', w='s')
# print(c)

e = {(43, 7): 1, (38, 7): 1}
print(type(e))
print(e)

# import ast
# s='{(43, 7): 1, (38, 7): 1}'
# d=dict(ast.literal_eval(s))
# print(d)
# d = eval('{(43, 7): 1, (38, 7): 1}')
# print(d)

subclass = 1
print(subclass)