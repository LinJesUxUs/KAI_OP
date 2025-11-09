buf = input("Введите целое число от 1 до 9: ")

try:
	x = int(buf)
	if 1 <= x <= 3:
		s = input("Введите строку: ")
		n = int(input("Введите число повторов строки: "))
		result = s
		for i in range(1,n):
			result += "\n" + s
		print(result)
	elif 4 <= x <= 6:
		m = int(input("Введите степень числа: "))
		x = x**m
		print(x)
	elif 7 <= x <= 9:
		for i in range(0,10):
			x+=1
			print( x )
	else: raise

except: print("Ошибка ввода")