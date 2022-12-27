#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
import random
n = int(input('введите число: '))
for i in range(n):
    print(random.randrange(-100, 100), end="; ")
