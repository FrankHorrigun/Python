# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random
n = int(input('введите количество арбузов: '))
list = [random.randint(1, 20) for i in range(1, n+1)]
print(list)
print(min(list), max(list))

