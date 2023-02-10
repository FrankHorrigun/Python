# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#  .е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = input('Введите номер билета: ')

if len(number)!=6:
    print('введите шетсизначное число')
number = int(number)
first =0
second =0
list_number=[]
while number>0:
    list_number.append(number%10)
    number//=10
print(list_number)
print(type(list_number))

for i in range(int(len(list_number)/2+1)):
    first += list_number[i]
    print(first)
    second +=list_number[:-i-1]
    print(second)
if first!=second:
    print('False')
else:
    print('True')
