# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.


str = str(input())
list = str.split()
print(list)
for i in range(len(list)):
    list[i] = int(list[i])
print(min(list), max(list))

list_num = input().split()
list_num = list(map(int, list_num))

str.strip