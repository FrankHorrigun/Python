# : На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# ыведите минимальное количество монет, которые нужно перевернуть.

import random
num = int(input('введите количество монеток: '))

list =[random.randint(0, 1) for i in range(num)]# ноль решка
print(list)

pos=0
for i in list:
    if i==0:
        pos+=1
if pos > len(list)/2:
    print(num - pos)
else:
    print(pos)
