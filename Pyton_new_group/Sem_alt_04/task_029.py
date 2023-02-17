# Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)

# import random
# list= [random.randint(0,100) for i in range(10)]
# # print(list)
# max = list[0]
# i=1

# while list[i] !=0:
#     print(i)
#     if list[i]>max:
#         max=list[i]
#         print(max)
#     if i<len(list)-1:
#         i+=1
#     else:
#         break

# print(list, max, sep='\n')

n = int(input())    
max=n
while n!=0:
    n = int(input())
    if n>max:
        max=n
print(max)
            