# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import datetime

# n = int(input())

# list = []

# def random_num():
#     rand_num = datetime.datetime.now().microsecond%10
#     return rand_num

# for i in range(n):
#     list.append(random_num())

# print(list)

random_num = datetime.datetime.now().microsecond % 10
print(random_num)
