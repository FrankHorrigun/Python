# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5
# 1 2 3 4 5
# 5
#  1 5 1 5 1
# Вывод: Вывод:
# 0 2

lst = [1, 5, 1, 2, 1, 6]
count = 0
# for i in range(1, len(lst)-1):
#     if lst[i-1]<lst[i]>lst[i+1]:
#         count+=1

# для закругленного
for i in range(len(lst)-1):
    if lst[i-1] < lst[i] > lst[i+1]:
        count += 1
if lst[len(lst)-2] < lst[len(lst)-1] > lst[1]:
    count += 1
print(count)

#alt optimal
for i in range(len(lst)):
    if lst[i-2]<lst[i-1]>lst[i]:
        count+=1
