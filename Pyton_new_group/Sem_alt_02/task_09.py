# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

number = int(input('Введите число: '))

mult=1
while number >0:
    mult*=number
    number-=1
print(mult)

for i in range(1, number+1):
    mult*=i