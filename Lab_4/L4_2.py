# 5. Вычислить элементы последовательности:
# a(0)=1;
# a(n)=a(n div 2)+a(n div 3), n>1;

from functions import getUIntWithMsg

print("Лаба-4. Задание-4.5")

def aRecurs(n):
	if n == 0:
		return 1
	return a( n // 2 ) + a( n // 3 )

def a(n):
	buf = {}
	buf[0] = 1
	for i in range(1,n+1):
		buf[i] = buf[i//2] + buf[i//3]
	return buf[n]

n = getUIntWithMsg("Введите длинну последовательности:","Введите целое целое!")
print("")

for i in range(n):
	print(aRecurs(i), end=" ")

print("")

for i in range(n):
	print(a(i), end=" ")

print("")

# print(aRecurs(1000000))
# print(a(1000000))