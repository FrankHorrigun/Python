# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input('введите число: '))
sum_of_digits = 0
while number % 10 != 0:
    sum_of_digits += number % 10
    number //= 10
print('сумма цифр', number, 'равна', sum_of_digits)
