# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Программа считает сумму цифр в трёхзначном числе!")
number = int(input("Введите трёхзначное число : "))
number1 = int(number // 100)
number2 = int(number // 10) % 10
number3 = int(number % 10)
result = number1 + number2 + number3
print("Сумма цифр : ")
print(result)