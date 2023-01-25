#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = [' wakl', 123, 'wabkjch', '123']
# a = 1234
# for i in range(len(list)):
#     if a== list[i]:
#         print('yes')

for item in list:
    if isinstance(item, int):
        print(item)
    else:
        print('false')