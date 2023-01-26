# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите номер ряда Фибоначчи: '))


fibonachi = [0, 1]
neg_fibonachi = []

# def fibonachi(n):
#     if n in (1,2):
#         return 1
#     return fibonachi(n-1)+fibonachi(n-2)


for i in range(2, n+1):# сделал обычный фибоначи
    fibonachi.append(fibonachi[i-1]+fibonachi[i-2])

for i in range(1, len(fibonachi)): #тут инвертировал знаки из обычного, функцию негафибоначи не допер как написать
    if i % 2 != 0:
        neg_fibonachi.append(-fibonachi[len(fibonachi)-i])
    else:
        neg_fibonachi.append(fibonachi[len(fibonachi)-i])

fibonachi_result = neg_fibonachi+fibonachi

print(fibonachi_result)


# def postive_fib(n): #решение препода
# postive_list = [0,1]
# for i in range(n-1):
# postive_list.append(postive_list[-2]+postive_list[-1])
# return postive_list
#
# def negative_fiv(n):
# negative_list = [0,1]
# for i in range(n-1):
# negative_list.append(negative_list[-2]-negative_list[-1])
# return negative_list
#
#
# print(negative_fiv(8)[::-1] + postive_fib(8)[1:])