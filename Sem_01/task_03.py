# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
n = int(input('введите число: '))
for i in range(-n, n+1):
    print(i, end = " ")
