#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = [' wakl', 123, 'wabkjch', '123']
# a = 123
# for i in range(len(list)):
#     if a== list[i]:
#         print('yes')

exist = False
for item in list:
    if isinstance(item, int):
        exist = True
    if isinstance(item, float):
        exist = True
print(exist)

for i in list:# либо так
    if type(i) == int:
        print(list.index(i))