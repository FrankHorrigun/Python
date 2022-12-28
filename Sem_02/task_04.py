# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random

def fullfill_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(-5, 5))
    return list


def find_qauntity_of_max_inlist(list):
    count = 0
    for i in range(len(list)-1):
        for j in range(i+1, len(list)-1):
            if list[i] == list[j]:
                count += 1
    return count


n = int(input('введите длину списка: '))
list = fullfill_list(n)
print(list, end="; ")
result = find_qauntity_of_max_inlist(list)
print(result)
