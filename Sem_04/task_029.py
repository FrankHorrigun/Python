# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('input 1 number: '))
b = int(input('input 2 number: '))

res = NULL
for i in range(9, 0):
    if a % i == 0 and b % i == 0:
        res = i
print(res)
