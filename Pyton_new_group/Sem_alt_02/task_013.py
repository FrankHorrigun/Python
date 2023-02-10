# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 найти продолжительность оттепели
# Output: 2

import random


def weater(n):
    list = [random.randint(-50, 51) for i in range(1, n+1)]
    return list


def ottepel(list):
    count=0
    for i in range(1, len(list)):
        if list[i] > 0 and list[i-1] > 0:
            count += 1
    return count


n = int(input('введите количество дней: '))
temp_list = []
ottepel_count = 0


if 1 <= n <= 100:
    temp_list = weater(n)
    print(temp_list)
    ottepel_count = ottepel(temp_list)
    print(ottepel_count)

else:
    print('введите число от 1 до ста')
