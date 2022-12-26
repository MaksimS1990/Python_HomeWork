# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.
# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

import os
os.system('cls')
from random import randint
import random

print("Программа ищет наиболее приближенный элемент в списке, относительно числа, который ввёл пользователь!")
print()

n = int(input("Введите длину списка N: "))
a = []

for i in range(0, n):                               # заполнение списка методом рандома
    random_num = round(random.randint(0, 5))
    a.append(random_num)
print(a)
print()
x = int(input("Введите искомое число X: "))

result = a[0]
count = abs(a[0] - x)
for i in range(0, len(a)):
    if count > abs(a[i] - x):
        result = (a[i])
        count = abs(a[i] - x)
    elif (abs(a[i] - x) == count):
        if result > a[i]:
            result = a[i]
        
print(f"Максимально близкое число к введённому Вами - {result}")