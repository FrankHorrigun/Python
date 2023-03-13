# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций.
# Ваша программа не должна быть линейной

def dct_write():
    with open('tel_dct.txt', 'a', encoding='UTF-8') as data:
        data.write(str(input('Введите ФИО и номер телефона через пробел: '))+'\n')
        data.write('\n')


def dct_read():
    with open('tel_dct.txt', 'r', encoding='UTF-8') as data:
        print(data.read())


def dct_search():
    with open('tel_dct.txt', 'r', encoding='UTF-8') as data:
        str1 = str(input('Введите элемент поиска: ')).lower()
        for i in data:
            if str1 in str(i).lower():
                print(i)


def dct_replace():
    with open('tel_dct.txt', 'r', encoding='UTF-8') as data:
        new_data = data.readlines()
        str1 = str(input('Введите элемент для поиска: '))
        str2 = str(input('Введите элемент для замены: '))
    with open('tel_dct.txt', 'w', encoding='UTF-8') as data:   
        for i in new_data:
            if str1 not in i:
                data.write(i)
            else:
                i = i.replace(str1, str2)
                data.write(i)
                # print(new_data)


def dct_remove():
    with open('tel_dct.txt', 'r', encoding='UTF-8') as data:
        new_data = data.readlines()
        # print(new_data)
        str1 = str(input('Введите элемент для удаления: '))
    with open('tel_dct.txt', 'w', encoding='UTF-8') as data:    
        for i in new_data:
            if str1 not in i:
                data.write(i)


print('Доступные операции: 1- новая запись, 2 - вывод справочника, 3 - поиск по справочнику, 4 - редактирование записи, 5 - удаление записи')
n = int(input('Введите номер операции: '))

if n == 1:
    dct_write()
elif n == 2:
    dct_read()
elif n == 3:
    dct_search()
elif n == 4:
    dct_replace()
elif n == 5:
    dct_remove()
else:
    print('Введите правильный код операции')
