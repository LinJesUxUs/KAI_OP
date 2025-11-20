from functions import randomList

print( "Лаба-3. Задание-3.10" )

A = randomList()

print("Исходный список\n",*A)

min_index = A.index( min([i for i in A if i>0]) )
max_index = A.index( max([i for i in A if i<0]) )

print("min_index =", min_index)
print("max_index =", max_index)

if min_index < max_index:
	A = A[0:min_index] + A[max_index:]
else:
	A = A[0:max_index] + A[min_index:]

print("Очищенный список\n",*A)
