import math

print("Лаба-2. Задание-1.10")

x = int(input("Введите X \n"))
n = int(input("Введите n \n"))

###################################

S = 0
count = 0
print("медленный способ")
for i in range(n+1):
    S += (((-1)**i) * x**(2*i) / math.factorial(2*i+1) )
    count += i * 5 + 2
    # i-1 степень + 1 + 2i степень с умножением
    #                       + 1 за деление + 2i+1 факториал

print("За", count, "операций умножения/деления.") 
print(S, "\nО-большое = O( (n*(n+1))/2 *5 + (n+1)*2 )")

#################################

print("оптимизированный способ")
S = 1
bufPow = 1
bufFac = 1
x2 = x ** 2
count = 1
for i in range(1,n):
    bufPow *= x2
    bufFac *= 2 * i
    bufFac *= ((2 * i) + 1)
    buf = bufPow / bufFac
    if i % 2 == 0:
        S += buf
    else:
        S -= buf
    count += 7
    # '*=' 3шт. '*' 2шт. '/' 1шт. '%' 1шт.

print("За", count, "умножений/делений.")
print(S, "\nО-большое = O( (n-1)*7 +1 )" )
