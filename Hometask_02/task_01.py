# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# классическое решение - переводим в инт
number = abs(float(input('введите число: ')))
len_number = len(str(number)) - 1
while number != int(number):
    number = round(number*10, len_number)

sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number //= 10
print('сумма цифр равна', sum_of_digits)

# решение через строку
N = input('Введите число: ')
summ = 0
for digit in N:
    if digit.isdigit():
        summ += int(digit)
print(summ)


# n = input('Введите число: ')  # еще решение
# n = [int(digit) for digit in n]
# summa = sum(n)
# print(n)
# print(summa)
