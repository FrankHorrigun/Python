# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3

n = int(input('input n: '))

num = 0
# count =0

while 2**num < n:
    print(num)
    num+=1
   
