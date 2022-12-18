# print('hello')
# типы данных int, float, string, boolean, list, NONE

# print('введите а')
# a = int (input())# по умолчанию тип строка, необходимо явно указывать тип данных
# print('введите b')
# b = int (input())
# s = 'hello world'
# f = True
# # аналог массива. рекомендуется создавать листы с данными одного типа
# list = [1, 2, 3]

# print('{} - {} - {}'.format(a, b, s))  # интерполяция
# print(f'{a} - {b} - {s}')  # интерполяция
# print('{2} - {1} - {0}'.format(a, b, s))  # интерполяция
# print(f)
# print(list)
# print('{} - {} '.format(a, b))
# print(a, ' + ', b, ' = ', a+b)

# арифметические операции
#  +, -, *, /, %, //, **
# / деление в вещественных числах, // деление в целых числах, ** возведение в степень
# round(a*b, 7) округление операции до 7 знаков после запятой

# логические операции
# >, >=, <, <=, ==, !=
# not, and, or не путать с &, |, ^
# is, is not, in, not in

# a = 1 < 4 and 5 > 2
# print(a)

# func = 1
# T = 4
# x = 2
# print(func < T > (x))

# f = [1, 2, 3, 4]
# print(not 2 in f)
# # is_odd = f[0] % 2 == 0 # проверка на четность, также 0 это ложь, а 1 истина
# is_odd = not f[0] % 2
# print(is_odd)

# if else

# `a = int(input('a = '))
# b = int(input('b = '))

# if a > b:
#     print('max = ', a)
# else:
#     print('max = ', b)

# username = input('Введите имя ')
# if username == 'Max':
#     print('Hi, Max')
# elif username == 'Frank':
#     print('Cheers, Frank')
# else:
#     print('FU,', username)

# while

original = 23
inverted = 0
while original != 0:
    inverted = inverted*10+(original % 10)
    original //= 10
    print(original)
else:
    print('stop')
print(inverted)
print()

# for i in enumeration

list = [1, 2, 3, 4, 5]
for i in list:
    print(i**2)
print()


for i in range(1, 10, 2):  # от 1 до 9 с шагом 2
    print(i)

for i in 'qwerty':
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)


# работа со строками

text = 'съешь еще этих мягких французских булок'
print(len(text))  # 39
print('еще' in text)  # true
print(text.isdigit())  # false
print(text.islower())  # true
print(text.replace('еще', 'ЕЩЁ'))   #

print(text[0])  # c
print(text[1])  # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])  # print(text)
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...


numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)  # [20, 4, 6, 8, 10] присваиет i значение, список не меняется
print(numbers)  # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue
for e in colors:
    print(e*2)  # redred greengreen blueblue
colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red')  # del colors[0] # удалить элемент

# функции


def f(x):
    return x**2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


print(f(1))  # Целое
print(f(2.3))  # 23
print(f(28))  # None
print(type(f(1)))  # str
print(type(f(2.3)))  # int
print(type(f(28)))  # NoneType


