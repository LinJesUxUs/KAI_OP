print( "Лаба-3. Задание-4" )

n = 0

while(True):
	try: n = int(input(
		"Введите предельное целое число последовательности.\n"))
	except: print("Введено не целое число!")
	else: break

# множество кратное 7
x = 7
st = {i for i in range(x,n,x)}

p = [i for i in range(2, n)]

for i in p:
	# итерация от 'p' в квадрате, так как 'p' простое число,
	# следующее кратное 'p' является квадратом 'p'
	for j in range(i**2, p[-1], i):
		try: p.remove(j)
		except: continue

print("Числа кратные",x,":",*st)
print("Простые числа:",*p)
