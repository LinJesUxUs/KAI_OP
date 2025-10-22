def check(a,b):
	if ( a < 0 ): return False
	elif ( b < 0 ): return False
	elif ( a <= b ): return False
	return True

A = int(input("Введите число A "))
B = int(input("Введите число B "))

if (check( A, B )):
	print("Отрезок \'B\'=", B,
		",на отрезке \'AB\'=", A+B,
		",помещается ", int((A+B) / B), "раз" )
else : print("Введены неверные данные")
