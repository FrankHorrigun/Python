# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

n = int(input())

lst=[]

for i in range(2,n):
    lst.append(n%i)
if 0 not in lst:
    print('true')
else:
    print('false')

   