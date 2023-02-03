#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

# через цикл
list_num = [random.randint(0,10) for i in range(random.randint(10, 50))]
print(list_num)

uniq_num_list=[]
for i in list_num:
    if i not in uniq_num_list:
        uniq_num_list.append(i)
print(uniq_num_list)

#через сет

uniq_num_list2 = list(set(list_num))
print(uniq_num_list2)

# не совсем понял условие. Здесь решение наоборот, выдаст список чисел, которые 1 раз повторяются в исходном (убираем все дубликаты)
list_num1 = [random.randint(0,10) for i in range(random.randint(5,6))]
print(list_num1)

uniq_num_list1=[num for num in list_num1 if list_num1.count(num) == 1]

print(uniq_num_list1)