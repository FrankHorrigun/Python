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

lst = input().lower().split()
print(lst, end='\n')

count = 0
for i in lst:
    for j in lst:
        if i == j:
            count+=1
            lst.remove(j)
            
print(count)
        
