# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random_index = []
uniq_random = random.randrange(0, len(list))

while len(random_index) < len(list):# тут свое решение предложил. перемешивает ВСЕ элементы списка
    while uniq_random in random_index:
        uniq_random = random.randrange(0, len(list))
    random_index.append(uniq_random)
# print(random_index)

for i in range(len(list)):
    temp = list[0]
    list[0] = list[random_index[i]]
    list[random_index[i]] = temp
print(list)