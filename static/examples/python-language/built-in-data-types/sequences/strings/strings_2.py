#!/usr/bin/env python3

# s = 'C:\Users\smirn\Documents\new\program.py'     # Выполнение этой инструкции возбудит исключение типа SyntaxError,
# print(s)                                          # поскольку обратные слеши интерпретируются
                                                    # как ведущие символы управляющих последовательностей

s = 'C:\\Users\smirn\Documents\new\program.py'      # Экранирование первого обратного слеша не решает все проблемы:
print(s)                                            # интерпретатор обнаружит управляющую последовательность '\n'
# Выведет две строки вместо одной:
# C:\Users\smirn\Documents
# ew\program.py

s = 'C:\\Users\\smirn\\Documents\\new\\program.py'  # Обратные слеши нужно экранировать,
print(s)                                            # если они не указывают на управляющие последовательности
# Выведет:
# C:\Users\smirn\Documents\new\program.py

s = r'C:\Users\smirn\Documents\new\program.py'      # Вместо экранирования обратных слешей можно воспользоваться
print(s)                                            # "сырыми" литералами строк
# Выведет:
# C:\Users\smirn\Documents\new\program.py
