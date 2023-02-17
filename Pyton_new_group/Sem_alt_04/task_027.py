# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

str = 'She sells sea shells on the sea shore The shells that she sells are sea shells'

# lst = input().lower().split()
# print(lst, end='\n')

list = str.lower().split()
print(list)
dct = {}

for i in list:# блять, сдесь не понял и сделал счетчик элементов, встречающихся 1 раз
    # добавление в словарь i - ключ,  dct[i] - значение +1
    dct[i] = dct.get(i, 0)+1
count = 0
for i in dct:  # i - ключ,  dct[i] - значение
    if dct[i] == 1:
        count += 1
        print(i, dct[i])

print(count)

print(set(list), len(set(list))) #тут список уникальных элементов

