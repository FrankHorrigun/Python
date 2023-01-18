# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число: '))
list = []
for i in range(-N, N+1):
    list.append(i)
print(list)

list_index = []
data = open('D:\Python\Hometask_02\input.txt', 'r')
for line in data:
    list_index.append(int(line))
data.close()
print(list_index)

composition_of_numbers = 1

for i in range(len(list_index)):
    if len(list) < list_index[i]+1:
        print('no elemensts in list')
    else:
        composition_of_numbers *= list[list_index[i]]
print(composition_of_numbers)
