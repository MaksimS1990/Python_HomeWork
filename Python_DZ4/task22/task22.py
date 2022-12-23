# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import os
os.system('cls')
from random import randint
import random

print('Программа вводит рандомом 2 неупорядоченных набора целых чисел и выдаёт в порядке возрастания те числа, которые встречаются в обоих наборах!')

number1 = int(input("Введите количество элементов первого набора : "))
n = []

for i in range(0, number1):                        # заполнение списка методом рандома
    random_num = round(random.randint(0, 9))
    n.append(random_num)
print(n)

number2 = int(input("Введите количество элементов второго набора : "))
m = []

for i in range(0, number2):
    random_num = round(random.randint(0, 9))
    m.append(random_num)
print(m)

count = 0
for i in range(0, len(n)):
    if n[i] == m[i]:
        count+=1
        i+=1
print(count)

temp = 0
for i in range(0, len(m)):
    if m[i] == n[i]:
        temp+=1
        i+=1
print(count)