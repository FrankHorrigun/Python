# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

week_day = int(input('введите день недели: '))
if 0 < week_day < 8:
    if week_day == 6 or week_day == 7:
        print('это выходной')
    else:
        print('рабочий день')
else:
    print('такого дня недели нет')
