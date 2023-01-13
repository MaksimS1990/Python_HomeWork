## Задача 26:  
## Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('cls')

a = int(input("Введите число a: "))
b = int(input("введите число b: "))

def exponentiation(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    elif b > 1:
        return (a * exponentiation(a, b-1))

print(f"Результат возведения в степень: {exponentiation(a, b)}")