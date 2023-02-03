# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

k = int(input('input k :'))

koeff_list = [randint(0,100) for i in range(0, k+1)]
# print(koeff_list)

polynomial=' + '.join([f'{(j)}*x**{i}' for i, j in enumerate(koeff_list)][::-1])
polynomial+=' = 0'
# Поиск и замены:
polynomial=polynomial.replace('x**1 +', 'x +')
polynomial=polynomial.replace('*x**0', '')

print(polynomial)

with open('polynomial2.txt', 'w') as data:
    data.write(polynomial)

