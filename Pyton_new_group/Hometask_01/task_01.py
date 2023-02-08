# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


n = int(input('введите чило: '))
print(sum(n))
