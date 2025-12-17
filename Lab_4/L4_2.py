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
	# if n in buf: return buf[n]
	for i in range(1,n+1):
		# if i not in buf:
		buf[i] = buf[i//2] + buf[i//3]
	return buf[n]

# buf = {}
# buf[0] = 1
# def a(n):
# 	global buf
# 	if n in buf: return buf[n]
# 	for i in range(1,n+1):
# 		if i not in buf:
# 			buf[i] = buf[i//2] + buf[i//3]
# 	return buf[n]

# n = getUIntWithMsg("Введите длинну последовательности:","Введите целое целое!")
# print("")

# for i in range(n):
# 	print(aRecurs(i), end=" ")

# print("")

# for i in range(n):
# 	print(a(i), end=" ")

# print("")

n = 10000
start = time.perf_counter()
for i in range(n):
	aRecurs(i)
print(f"aRecurs({n}): {(time.perf_counter()-start):.6f} seconds")
start = time.perf_counter()
for i in range(n):
	a(i)
print(f"a({n}): {(time.perf_counter()-start):.6f} seconds")
start = time.perf_counter()
for i in range(n):
	aRecurs(i)
print(f"aRecurs({n+1}): {(time.perf_counter()-start):.6f} seconds")
start = time.perf_counter()
for i in range(n):
	a(i)
print(f"a({n+1}): {(time.perf_counter()-start):.6f} seconds")