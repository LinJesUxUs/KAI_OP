# 2. Задан орграф в виде количества вершин n<=10 и последовательности дуг
# (дуга задается парой “предшественник преемник”).
print("Лаба-4. Задание-4.2")

import random
from functions import getUIntWithMsg
from functions import getBoolVal

G = {}

print("Построить граф случайно?")
if (getBoolVal()):
	n = random.randint(1,10)
	for u in range(n):
		for v in range(n-1):
			if (not random.choice([True, False])):
				continue
			if u not in G:
				G[u] = {}
			G[u][v] = 1
else:
	while(True):
		M = getUIntWithMsg("Введите колличество рёбер графа:","Введите целое целое!")
		for i in range(M):
			u,v = input("Введите пару индексов вершин 'u' и 'v' ребра:").split()
			try:
				u = abs(int(u))
				v = abs(int(v))
				if u not in G:
					G[u] = {}
				G[u][v] = 1
			except:
				print("'u' или 'v' не целое число")
		
		print("Есть ещё рёбра для ввода?")
		if (not getBoolVal()):
			break

print(G)

print("а) номера вершин, имеющих более двух преемников:")

for u in G:
    if (len(G[u]) > 2 ):
        print(u, end=" ")
print(" ")

print("б) Напечатать номера вершин, не имеющих предшественников")

endV = []
for u in G:
    for v in G[u]:
        if ((v not in G) and (v not in endV)):
            endV.append(v)
print(*endV)

print("в) Для каждой вершины напечатать номера всех предшественников.")

buf = []
for u in G:
    for v in G[u]:
        if (v not in buf):
            buf.append(v)
for i in buf:
    endV.clear()
    for u in G:
        if (i in G[u]):
            endV.append(u)
    print(i, endV)

print("г) Проверить, есть ли в графе вершины, имеющие только одного преемника.")

found = False
endV.clear()
for u in G:
    if (len(G[u]) == 1 ):
        endV.append(u)
        found = True

if not found:
    print("Нет.")
else:
    print(*endV)
