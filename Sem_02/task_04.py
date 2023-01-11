# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random

def fullfill_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(-5, 5))
    return list


def find_qauntity_of_max_inlist(list):# тут не совсем задание понял, просто вообще количество одиновых ищет
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

# list_num = []  # решение препода через создание сета. Сет фильтрует одинаковые значения списка, но список не меняет
# max = 0
# for i in range(10):
# a= random.randint(2,5)
# list_num.append(a)
# print(list_num)
# print(set(list_num))
# for i in set(list_num):
# if list_num.count(i)>max:
# max = list_num.count(i)
# print(max)




# a = 1
# b = 6

# array = [random.randint(a, b) for i in range(20)]   # решение через словарь
# print(array)

# print(set(array))
# d = {}

# for i in array:
# if i in d:
# d[i] += 1
# else:
# d[i] = 1

# print(d)

# max = 0
# for i in range(a, (b + 1)):
# if (d[i] > max):
# max = d[i]

# print(f"Максимальное повторение элемента {max} раз.")



## сортировкой
number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
list.append(random.randint(0, maxRandom))

for i in list:
count[int(i)] += 1

for i in count:
if i > maxAmount:
i = maxAmount

print(list)
print(max(count))
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')