# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list =  ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list2 = "qwe"
second_index = []
for i in range(len(list)):
    if list2 == list[i]:
        second_index.append(i)
print(second_index[1])
