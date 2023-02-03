# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число n: '))

list_simple_mult = []
mult = 2
while mult*mult <= n:
    print('mult=', mult)
    if n % mult == 0:
        list_simple_mult.append(mult)
        n//=mult
        print('n=', n)
    else:    
        mult += 1
if n>1:
    list_simple_mult.append(n)
print(list_simple_mult)
