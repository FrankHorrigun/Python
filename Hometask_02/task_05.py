# Реализуйте алгоритм перемешивания списка.

import random
list = [10, 5, 3, 4, 8]

random_index = [len(list)]
random_index[0] = random.randrange(0, len(list))
for i in range(1, len(random_index)):
    x = random.randrange(1, len(list))
    if x not in random_index[i:len(random_index)]:
        random_index[i] = x
print(random_index)
