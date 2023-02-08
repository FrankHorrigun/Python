# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y

# def mult(x, y):
#     return x*y

# def calc(op, a, b):# в качестве аргумента можно передать функцию
#     print(op(a, b))

# calc(mult, 4, 5)
# calc(lambda x, y: x+y, 4, 5)

# List Comprehention

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp (if conditional) for item in iterable (if conditional)]

# list = []
# for i in range(1, 101):
#     if i%2 == 0:
#         list.append(i)
# print(list)

# list = [i for i in range(1, 21) if i%2 ==0]
# list = [(i, i) for i in range(1, 21) if i%2 ==0]#tuple
# print(list)

# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 21) if i%2 ==0]
# print(list)

# Задача
# В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадрат числа)

# 1 2 3 5 8 15 23 38

# list = [1, 2, 3, 5, 8, 15, 23, 38]

# result = [(i, i**2) for i in list if i % 2 == 0]
# print(result)

# path = ''
# f = open(path, 'r')
# data = f.read + ' '
# f.close

# numbers = []
# while data != '':# пока строка не пустая
#     space_pos= data.index(' ')# находим первую позицию пробела
#     numbers.append(int(data[:space_pos]))# добавляем элемент до позиции пробела с переводом в инт
#     data = data[space_pos+1]#

# out = []
# for e in numbers:
#     if not e %2:
#         out.append((e, e**2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'. split()  # получаем список строк
# print(data)
# res = select(int, data)  # получаем список чисел
# print(res)
# res = where(lambda x: not x % 2, res)  # получаем список четных чисел
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# li = [x for x in range(1, 20)]
# print(li)
# li =list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int, input().split()))# преобразовывает ввод с клавы с разделителем по пробелу в список чисел

# map - итератор, работает 1 раз. поэтому если нужно, сохраняем значения в списке например черех присваивание list(map(f, iterable))

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'. split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x:(x, x**2), res))
# print(res)

#Фуникция Zip, применяется к набору итерируемых данных и возвращает итератор с кортежами из входных данных. Проходит по минимальному набору данных

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

#Фуникция Enumerate, применяется к набору итерируемых данных и возвращает новый итератор с кортежами из индекса и элементов входных данных.
users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)