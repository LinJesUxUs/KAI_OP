import math

a = int(input("Введите катет \'a\' "))
print("Введён катет \'a\' = ", a)
b = int(input("Введите катет \'b\' "))
print("Введён катет \'b\' = ", b)
c = math.sqrt(( a ** 2 )+( b ** 2 ))
P = a + b + c
print("Гипотенуза \'c\' равна = ", c )
print("Периметр \'P\' равен = ", P )