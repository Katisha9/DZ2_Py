# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')
summDigit = 0

for digit in number:
    if digit.isdigit():
        summDigit += int(digit)

print(f"Сумма цифр числа {number} равна", summDigit)