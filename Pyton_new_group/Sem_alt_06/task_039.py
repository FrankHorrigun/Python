# аны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

lst1 = [3,1,3,4,2,4,12]
lst2 = [4,15,43,1,15,1]

# set1=set(lst1)
# set2 = set(lst2)
res=[]
for i in lst1:
    if i not in lst2:
        res.append(i)
print(res)
