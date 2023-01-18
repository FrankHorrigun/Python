# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# number = abs(int(input('введите число: ')))  # классическое решение для int
# sum_of_digits = 0
# while number > 0:
#     sum_of_digits += number % 10
#     number //= 10
# print('сумма цифр равна', sum_of_digits)

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
