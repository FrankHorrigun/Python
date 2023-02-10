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
    count =0
    result=[]
    for i in range(len(list)):
        if list[i]>0:
            count =1
            for i in range(i+1, len(list)):
                if list[i] > 0 and list[i-1] > 0:
                    count += 1
                result.append(count)
    return result


n = int(input('введите количество дней: '))
temp_list = []
ottepel_count = 0


if 1 <= n <= 100:
    temp_list = weater(n)
    print(temp_list)
    print(ottepel(temp_list))
    ottepel_count = max(ottepel(temp_list))
    print(ottepel_count)

else:
    print('введите число от 1 до ста')


day = int(input())
k = 0
max = 0
for i in range(day):
temp = int(input())
if temp > 0:
k += 1
else:
if max < k:
max = k
k = 0
