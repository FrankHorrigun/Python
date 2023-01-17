# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число: '))
list = []
for i in range[-N, N+1]:
    list.append(i)
print(list)

list_index = []
data = open(D:\учеба\Python\Hometask_02.input.txt)
for line in data:
    list_index.append(int(line))
data.close()

composition_of_numbers = 0

for i in range(len(list_index)+1):
    if len(list) < list_index(i):
            print('no elemensts in list')
    else:    
        composition_of_numbers *= list[list_index]
    print(composition_of_numbers)
