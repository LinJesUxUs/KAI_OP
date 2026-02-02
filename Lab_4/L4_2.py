# 5. Вычислить элементы последовательности:
# a(0)=1;
# a(n)=a(n div 2)+a(n div 3), n>1;

from functions import getUIntWithMsg
import time
print("Лаба-4. Задание-4.5")

def aRecurs(n):
	if n == 0:
		return 1
	return aRecurs( n // 2 ) + aRecurs( n // 3 )

def a(n):
	buf = {}
	buf[0] = 1
	lst = []
	i = n
		
	for i in range(n,1,-1):
		lst.append(i)
	for i in range(1,n+1):
		if i not in buf:
			buf[i] = buf[i//2] + buf[i//3]
	return buf[n]

n = getUIntWithMsg("Введите длинну последовательности:","Введите целое целое!")
# n = 10000

print()

start = time.perf_counter()
v = aRecurs(n)
print(f"aRecurs({n}) = {v}\t: {(time.perf_counter()-start):.6f} seconds")

start = time.perf_counter()
v = a(n)
print(f"a({n}) = {v}      \t: {(time.perf_counter()-start):.6f} seconds")
