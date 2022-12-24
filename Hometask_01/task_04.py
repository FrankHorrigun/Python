# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quater_number = int(input('введите номер четверти: '))
if quater_number == 0:
    print('0')
elif quater_number == 1:
    print('x>0, y>0')
elif quater_number == 2:
    print('x<0, y>0')
elif quater_number == 3:
    print('x<0, y<0')
elif quater_number == 4:
    print('x>0, y<0')
