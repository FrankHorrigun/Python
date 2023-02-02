# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. nok = a*b/nod(a, b)

a = int(input('input 1 number: '))
b = int(input('input 2 number: '))

nod =1#наибольший общий делитель

for i in range(a*b+1, 2, -1):
    if a % i == 0 and b % i == 0:
        nod = i
        break

nok = int(a*b/nod)
print(nok)

a = int(input())
b = int(input())
for i in range(max(a,b),a*b,max(a,b)):
    print(i)
    if i%a==0 and i%b==0:
        print(i)
        