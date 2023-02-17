# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12
def create_list(x):
    lst = []
    for i in range(x):
        lst[i] = int(input('введите число: ', i+1))
    return lst


def dizz(lst1, lst2):
    new_set = set()
    for i in lst1:
        if i in lst2:
            new_set.add(i)
    return new_set


def sort(new_set):

    for i in range(len(new_set)):
        for j in range(i, len(new_set)):
            if new_set[i] > new_set[j]:
                new_set[i], new_set[j] = new_set[j], new_set[i]
    return new_set


# n = int(input('введите длину первого набора чисел: '))
# m = int(input('введите длину второго набора чисел: '))
# lst1 = create_list(n)
# lst2 = create_list(m)
lst1=[2,4,5,8,10,12,10,8,6,4,2]
lst2=[3,6,9,12,15,18]

new_set = set()

if len(lst1) > len(lst2):
    new_set = dizz(lst1, lst2)
else:
    new_set = dizz(lst2, lst1)
new_set=sort(new_set)
print(new_set)
