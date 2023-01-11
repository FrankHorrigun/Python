# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random


def fullfill_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(-5, 5))
    return list


n = int(input('введите длину списка: '))
list = fullfill_list(n)
print(list)

max = 0
for i in range(n-1):
    if list.count(list[i]) > max:
        max= list.count(list[i])
print(max)
