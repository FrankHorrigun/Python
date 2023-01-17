# Задайте список из n чисел последовательности $(1+1\n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}


n = int(input('Введите число: '))

result = {i: (1+1/i)**i for i in range(1, n+1)}
sum = 0
for i in range(1, len(result)+1):
    sum += result[i]

print(result)
print(sum)
