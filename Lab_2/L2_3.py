import math

print( "Лаба-2. Задание-3" )

lst = [""] #объявление пустого листа
while True:
    lst = input(
        "Введите 6 целых десятичных чисел через запятые:\n").split(',')
    
    if (len(lst) != 6 ):
        print("Введено не 6 чисел!")
        continue
    
    lbuf = "" # буфер для вывода неправильного элемента
    try:
        for l in lst:
            lbuf = l
            i = int(l) # проверка на целочисленность
    except:
        print(lbuf, "не является числом")
        continue
    
    break

print( "а) ", lst[4] )
print( "б) ", lst[::-1] )

s = 0
for l in lst:
    s += int(l)
print("Сумма чесел =", s, "\nСреднее арифметическое =", s/6 )