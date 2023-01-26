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


for i in range(2, n+1):
    fibonachi.append(fibonachi[i-1]+fibonachi[i-2])

for i in range(1, len(fibonachi)):
    if i % 2 != 0:
        neg_fibonachi.append(-fibonachi[len(fibonachi)-i])
    else:
        neg_fibonachi.append(fibonachi[len(fibonachi)-i])

fibonachi_result = neg_fibonachi+fibonachi

print(fibonachi_result)
