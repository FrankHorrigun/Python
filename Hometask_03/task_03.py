# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

max = list[0] % 1
min = list[0] % 1

for i in range(1, len(list)):# можно записать итерацию сразу элементов for i in list// тогда везде list[i] заменить на i
    if list[i] %1 !=0:
        list[i] = round(list[i]%1, 2)
        if max < list[i]:
            max = list[i]
        if min > list[i]:
            min = list[i]
print('max= ', max)
print('min= ', min)
print(max-min)

