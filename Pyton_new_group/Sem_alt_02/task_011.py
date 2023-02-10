# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# def fibonachi(n):
#     if n in (1,2):
#         return 1
#     return fibonachi(n-1)+fibonachi(n-2)
        

n = int(input('введите число: '))
# i =1
# while fibonachi(i)<a:
#     if fibonachi(i)==a:
#         print('true', i)
#     else:
#         print('false')
#     i+=1

n = int(input())
n0 = 0
n1 = 0
n2 = 1
i = 2
while n0 < n:
n0 = n1 + n2
n1 = n2
n2 = n0
i += 1
if n0 > n:
i = 0
if i != 0:
print(i)
else:
print(-1)

