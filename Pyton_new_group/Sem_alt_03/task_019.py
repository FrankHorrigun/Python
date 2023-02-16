# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
steps=3
if steps < 0:
    steps = abs(steps)
    for i in range(steps):
        list.append(list.pop(0))
        print(list, 'app')
else:
    for i in range(steps):
        list.insert(0, list.pop())
        print(list, 'ins')
print(list)

# # append - добавляет элемент в конец списка,
# # insert - вставляет элемент по указанному индексу,
# # pop - извлекает элемент с конца списка или, если был передан индекс, по индексу.

length = int(input())
lst = list(map(int, input().split()))
shift = int(input())

lst = lst[-shift:] + lst[:-shift]

print(lst)


