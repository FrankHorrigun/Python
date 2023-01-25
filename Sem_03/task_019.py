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

n = input()
random_num = datetime.datetime.now().microsecond % (n+1)# остаток от числа в диапазоне от 0 до n
print(random_num)
