# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 3
# 1 2 3 4 5
# Вывод: 1

import os
os.system('cls')
from random import randint
import random

n = int(input("Введите длину списка: "))
x = int(input("Введите искомое число: "))
a = []

for i in range(0, n):                                   # заполнение списка методом рандома
    random_num = round(random.randint(0, 5))
    a.append(random_num)
print(a)

count = 0
for i in range(0, len(a)):
    if a[i] == x:
        count+=1

print(f"Искомое Вами число встречается {count} раз")