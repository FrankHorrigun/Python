# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]


def Composition_of_elements(list):
    composition = []
    pivot = 0 # не оптимально, но как решил так решил, надо было сразу его задать как len(list)//2 + len(list)%2
    if len(list) % 2 != 0:
        pivot = int(len(list)/2+1)
    else:
        pivot = int(len(list)/2)

    for i in range(pivot):
        composition.append(list[i]*list[len(list)-i-1])
    return composition 


print(Composition_of_elements(list1))
print(Composition_of_elements(list2))
