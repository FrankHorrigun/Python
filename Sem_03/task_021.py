# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list =  ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list2 = "qwe"
second_index = []
for i in range(len(list)):
    if list2 == list[i]:
        second_index.append(i)
print(second_index[1])


# list_str = []
# sub_str = "123"
# count = 0
# for i in range(len(list_str)):
#   print(i)
#   if list_str[i]==sub_str:
#       count+=1
#   if count == 2:
#       print(i)
#       break
#   if count<2:
#       print(-1)