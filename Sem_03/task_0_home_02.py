# Реализуйте алгоритм перемешивания списка.

import random
import datetime

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list)
print(list)

print(datetime.datetime.now().microsecond)


def random_num(max_num):
    random_num = datetime.datetime.now().microsecond/10**6
    return random_num*max_num


for i in range(len(list)-1, -1, -1):

    j = int(random_num(i+1))
    a[i], a[j] = a[j], a[i]
