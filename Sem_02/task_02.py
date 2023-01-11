# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

n = int(input('введите число: '))
list = [n+1]
for i in range(1, n+1):
    list.append(3*i+1)
    print(i, ':', list[i], '; ', end=" ")

# ipanarot slovar
print()
a = {}  # задаем словарь синтаксис a{i, x} i - ключ, а х значение
n = int(input('введите число: '))
for i in range(1, n+1):
    a[i] = n*3+1
print(a)


#print (one_str.count (two_str)) короткое решение за счет встроенной функции каунт