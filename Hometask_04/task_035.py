# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('polynomial1.txt', 'r') as data:
    poly1 = data.readline()

with open('polynomial2.txt', 'r') as data:    
    poly2 = data.readline()

print(poly1, poly2, sep='\n')

for i in min(poly1, poly2):
    print(i)
