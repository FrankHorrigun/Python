# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.

x = int(input("x="))
y = int(input("y="))
# s = int(input("s="))
# p = int(input("p="))
# kate = int(input("kate="))

# if kate == x+y and x*y:
for i in range(x):
    for j in range(y):
        if x == i+j and y == i*j:
            print('угадала', i, j)
