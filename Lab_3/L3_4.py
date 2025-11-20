
print( "Лаба-3. Задание-4" )

n=0

while(True):
	try: n = int(input(
		"Введите предельное целое число последовательности."))
	except: print("Введено не целое число!")
	else: break

st = {i for i in range(2,n)}
lst = []

for i in range(2,n): #нужно i домножать на 2 при итерации


print(*st)