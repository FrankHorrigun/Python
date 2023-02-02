#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число n: '))

list_simple_num=[1]
for i in range(1,n+1):
    for j in range(0,i+1):
        if i%list_simple_num[j]==0:
            list_simple_num.append(i)
print(list_simple_num)

