# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def convert(poly):
    poly = poly.replace('x + ', 'x**1 + ').replace(' x', ' 1*x').replace(' = 0', '*x**0')
    poly = poly.replace(' + ', ' +').replace(' - ', ' -').replace('x**', '')
    poly = poly.split()
    dict_poly = {}
    for i in range(len(poly)):
        poly[i] = poly[i].replace('+', '').split('*')
        dict_poly[int(poly[i][1])] = int(poly[i][0])
    return dict_poly


def sum_poly(dict1, dict2):
    dict_result = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)#штобы получить значение None
        second = dict2.get(i)
        if first != None or second != None:
            dict_result[i] = (first if first != None else 0) + \
                (second if second != None else 0)
    return dict_result

def convert_dict_to_poly(dict_result):
    result =''
    for i in dict_result.items():
        if i [1] <0:# если значение меньше нуля ([0] - keys, [1]-values)
            result += ' - ' + str(abs(i[1])) + '*x**' + str(abs(i[0]))
        elif i[1] > 0:
            result += ' + ' + str(abs(i[1])) + '*x**' + str(abs(i[0]))
    result = result.replace('x**1 ', 'x ').replace('*x**0', '').replace(' 1*x', 'x') + ' = 0'
    if result[1] == '+':
         result = result[3:]     
    else:
        result = result[1:]
    return result

with open('polynomial1.txt', 'r') as data:
    poly1 = data.readline()

with open('polynomial2.txt', 'r') as data:
    poly2 = data.readline()

print(poly1, poly2, sep='\n')

dict1 = convert(poly1)
dict2 = convert(poly2)
# print(dict1)
# print(dict2)
dict_result = sum_poly(dict1, dict2)
# print(dict_result)
result_poly = convert_dict_to_poly(dict_result)
print(result_poly)

with open('poly_summ.txt', 'w') as data:
    data.write(result_poly)
