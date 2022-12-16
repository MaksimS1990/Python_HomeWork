# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint
import random

print("Программа определяет минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной стороной!")
number = int(input("Введите количество монеток : "))
n = []
result = 0
count = 0
min = 0
for i in range(0, number):                        # заполнение списка методом рандома
    random_num = round(random.randint(0, 1))
    n.append(random_num)
print(n)
for i in range(0, number):
    if n[i] == 1:
        result+=1
print(result)
for i in range(0, number):
    if n[i] == 0:
        count+=1
print(count)
if result < count:
    min = result
else:
    min = count
print(f"Монеток, которые Вам необходимо перевернуть - {min}")