#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
def input_number(string):
    get_number = int(input(string))
    return get_number
def find_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance
x1 = input_number('введитете координаты x1: ')
y1 = input_number('введитете координаты y1: ')
x2 = input_number('введитете координаты x2: ')
y2 = input_number('введитете координаты y2: ')
distance = find_distance(x1, y1, x2, y2)
print('расстояноятие между точками равно', distance)

