# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 
# a=b= c/(a+b)/2
#a+b+(a+b)*2 =s
# a=b
# a+a+(a+a)*2 =s
#6a = s
#a=b= s/6
#c= 4*a= s/6*4=s*2/3


sum = int(input('количество журавликов: '))
print('Петя:', int(sum/6), 'Катя:', int(sum*2/3), 'Сережа:', int(sum/6))



