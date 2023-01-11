# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

def Count_of_insertions(text1, text2):
    count = 0
    for i in range(len(text1)-len(text2)+1):
        if text1[i:i+len(text2)] == text2: # len(text2) - это дли подстроки. диапазон начиная с I и заканчивая i+len(text2)
            count += 1
    return count


input1 = (input(''))
input2 = (input(''))

print('в', input1, 'находится', input2,
      Count_of_insertions(input1, input2), 'раз')
print('в', input2, 'находится', input1,
      Count_of_insertions(input2, input1), 'раз')
