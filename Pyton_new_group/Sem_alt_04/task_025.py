# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# list = input().split()
list = 'a a a b c a a d c d d'
print(list)
dict = {list[0]: [1]}
x=1
for i in list:
    if i in dict:
        x+=1
        dict.update([i])
print(dict)
