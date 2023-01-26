# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число: '))
print('control', bin(N))

result = ''
while N > 0:
    result = str(N % 2) + result
    N = N//2
    
print('result', result)

