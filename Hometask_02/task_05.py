# Реализуйте алгоритм перемешивания списка.

import random
list = [10, 5, 3, 4, 8]

random_index = []
uniq_random = random.randrange(0, len(list))

while len(random_index) < len(list):
    while uniq_random in random_index:
        uniq_random = random.randrange(0, len(list))
    random_index.append(uniq_random)
# print(random_index)

for i in range(len(list)):
    temp = list[0]
    list[0] = list[random_index[i]]
    list[random_index[i]] = temp
print(list)