## Задача 28:
## Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
## Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import os
os.system('cls')

a = int(input("Введите первое число a: "))
b = int(input("введите второе число b: "))

def Sum (a, b):
    if b > 0:
        return Sum(a+1, b-1)
    else:
        return a
print (f"Сумма Ваших чисел равно: {Sum(a, b)}")