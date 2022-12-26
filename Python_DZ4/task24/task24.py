# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
#Input: 4
#(значения сгенерированы случайным образом
#4 2 3 1 )
# Output: 9

import os
os.system('cls')
from random import randint
import random

print('Программа находит максимальноое числа ягод,которое может собрать за один заход собирающий модуль, находясь перед кустом заданной во входном файле грядки!')

n = int(input('Введите количество кустов на грядке : '))

list = []

for i in range(0, n):                             # заполнение списка методом рандома
    random_number = round(random.randint(0, 10))
    list.append(random_number)
print(list)

result = 0
max = list[0] + list[1] + list[2]
for i in range(n - 1):
    m = list.pop()
    list.insert(0, m)
    result = list[0] + list[1] + list[2]
    if result > max:
        max = result

print(max)