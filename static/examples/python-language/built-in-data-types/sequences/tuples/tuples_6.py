#!/usr/bin/env python3

# Задаём кортеж с пятью уровнями вложенности
a = (
    '0',
    (
        '1_0',
        '1_1',
        (
            '1_2_0',
            '1_2_1',
            '1_2_2',
            (
                '1_2_3_0',
                '1_2_3_1',
                '1_2_3_2',
                '1_2_3_3',
                (
                    '1_2_3_4_0',
                    '1_2_3_4_1',
                    '1_2_3_4_2',
                    '1_2_3_4_3',
                    '1_2_3_4_4',
                    '1_2_3_4_5',
                ),
                '1_2_3_5',
                '1_2_3_6',
                '1_2_3_7',
                '1_2_3_8',
            ),
            '1_2_4',
            '1_2_5',
            '1_2_6',
        ),
        '1_3',
        '1_4',
    ),
    '2',
)

# Обход всех элементов кортежа в цикле с проверкой элементов на принадлежность к типу tuple
for i, e0 in enumerate(a):
    if isinstance(e0, tuple):
        for j, e1 in enumerate(e0):
            if isinstance(e1, tuple):
                for k, e2 in enumerate(e1):
                    if isinstance(e2, tuple):
                        for m, e3 in enumerate(e2):
                            if isinstance(e3, tuple):
                                for n, e4 in enumerate(e3):
                                    print(f'a[{i}][{j}][{k}][{m}][{n}] = {e4}')
                            else:
                                print(f'a[{i}][{j}][{k}][{m}] = {e3}')
                    else:
                        print(f'a[{i}][{j}][{k}] = {e2}')
            else:
                print(f'a[{i}][{j}] = {e1}')
    else:
        print(f'a[{i}] = {e0}')
# Выведет:
# a[0] = 0
# a[1][0] = 1_0
# a[1][1] = 1_1
# a[1][2][0] = 1_2_0
# a[1][2][1] = 1_2_1
# a[1][2][2] = 1_2_2
# a[1][2][3][0] = 1_2_3_0
# a[1][2][3][1] = 1_2_3_1
# a[1][2][3][2] = 1_2_3_2
# a[1][2][3][3] = 1_2_3_3
# a[1][2][3][4][0] = 1_2_3_4_0
# a[1][2][3][4][1] = 1_2_3_4_1
# a[1][2][3][4][2] = 1_2_3_4_2
# a[1][2][3][4][3] = 1_2_3_4_3
# a[1][2][3][4][4] = 1_2_3_4_4
# a[1][2][3][4][5] = 1_2_3_4_5
# a[1][2][3][5] = 1_2_3_5
# a[1][2][3][6] = 1_2_3_6
# a[1][2][3][7] = 1_2_3_7
# a[1][2][3][8] = 1_2_3_8
# a[1][2][4] = 1_2_4
# a[1][2][5] = 1_2_5
# a[1][2][6] = 1_2_6
# a[1][3] = 1_3
# a[1][4] = 1_4
# a[2] = 2