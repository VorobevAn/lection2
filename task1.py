
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


num = (input("Введите чило: "))

number = num.split('.')
summ = 0

if len(number) == 1:
    c = int(number[0])
    while (c != 0):
        summ += c % 10
        c=c//10
else:
    a = int(number[0])
    b = int(number[1])

    while (a != 0):
        summ += a % 10
        a = a//10

    while (b != 0):
        summ += b % 10
        b = b//10
print(f'Сумма цифр числа: {summ}')
