# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import random
col = [random.randint(-5, 6) for i in range(10)]
uniq = list(set(col))
print(col, uniq, len(uniq), sep='\n')

result =[]
for i in col:
    if i not in result:
        result.append(i)
 
print(col, len(result), sep='\n')
