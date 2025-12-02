# 2. Задан орграф в виде количества вершин n<=10 и последовательности
# дуг (дуга задается парой “предшественник преемник”).
#  а) Напечатать номера вершин, имеющих более двух преемников.
#  б) Напечатать номера вершин, не имеющих предшественников.
#  в) Для каждой вершины напечатать номера всех предшественников.
#  г) Проверить, есть ли в графе вершины, имеющие только одного
# преемника.
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

def rep(graf, n):
    for i in range(n):
        for j in range(n):
            graf[i][j]=max(graf[i][j],graf[j][i])
            graf[i][j]=max(graf[i][j],graf[j][i])
    return graf

n, k = map(int, input('Введите n и k: ').split())

"""
Ввод графа
"""
print("Выберите способ ввода графа:\n1) Матрица смежности\n2) Рандомно сгенерировать\n3) Матрица инцидентности")
var_input=int(input("Вариант "))
graf=[[0 for i in range(n)]for i in range(n)]
if var_input==1:
    print("Вводите каждую строку матрицы смежности, разделяя числа пробелом:")
    for i in range(n):
        a=input().split(' ')
        graf.append(a)
    time.sleep(1)
elif var_input == 2:
    print('Граф будет сгенерирован автоматически')
    graf=[[0 for i in range(n)]for j in range(n)]
    max_connect=max(k//(2*n), 1)
    count=0
    for i in range(n):
        for j in range(n):
            a=random.randint(0,max_connect)
            if count+a<=k and j>=i:
                count+=a
                graf[i][j]=a
            elif count+a>k and count<k and j>=i:
                graf[i][j]=k-count
                count=k
    graf=rep(graf, n)
    while count<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if b>=a:
            graf[a][b]+=1
            count+=1
elif var_input==3:
    print('Введите матрицу инцидентности')
    print("*", end='  ')
    for i in range(k):
        print(f'{i}', end=' ')
    print('')
    edges=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        print(f'{i}: ', end='')
        edges[i]=input().split()

if var_input != 4: graf=rep(graf, n)
else:
    for j in range(k):
        fv=-1
        sv=-1
        for i in range(n):
            if edges[i][j]=='1' and fv==-1:
                fv=i
            elif edges[i][j]=='1' and fv!=-1:
                sv=i
                graf[fv][sv]+=1
                graf[sv][fv]+=1
                fv=-1
                sv=-1
            elif edges[i][j]=='2':
                graf[i][i]+=1

#Сюда надо добавить создание edges - матрицы инцедентности, если применяется другой ввод, 
#ибо эта матрица используется дальше в коде для получения ответов на некоторые задания

#Ребра
edge_1=[]#В i-ой ячейке одна часть ребра
edge_2=[]#В i-ой ячейке вторая часть ребра
for i in range(n):
    for j in range(n):
        if graf[i][j]!=0:
            for k in range(graf[i][j]):
                edge_1.append(i)
                edge_2.append(j)
                edge_1.append(j)
                edge_2.append(i)

#Задание 1
print("\n------------------------\n")
print("Ответ на первое задание:")
vers=[0 for i in range(n)]
five=[0 for i in range(n)]
for i in range(n):
    print(f'Вершине {i} инцеденты ребра: ', end='')
    for j in range(k):
        if edges[i][j]!='0':
            print(j,end=' ')
            vers[i]+=1
            five[i]+=1
        if edges[i][j]=='2':
            vers[i]+=1
    print('')
time.sleep(0.5)

#Задание 2
print("\n------------------------\n")
print("Ответ на второе задание:")
for i in range(len(vers)):
    print(f'Степень вершины {i} = {vers[i]}')
time.sleep(0.5)

#Задание 3
print("\n------------------------\n")
print("Ответ на третье задание:")
if 0 in vers:
    print('Существует вершина со степенью 0')
else:
    print('Не существует вершины со степенью 0')
time.sleep(0.5)

#Задание 4
print("\n------------------------\n")
print("Ответ на четвертое задание:")
four=0
for i in edges:
    if i.count('1')+i.count('2')==1:
        four+=1
print(f'{four} вершин инцедентны только одному ребру')
time.sleep(0.5)

#Задание 5
print("\n------------------------\n")
print("Ответ на пятое задание:")
print(f'максимум смежных ребер, инцедентных одной вершине - {max(five)}')
time.sleep(0.5)

#Задание 6
print("\n------------------------\n")
print("Ответ на шестое задание:")
for i in range(n):
    if graf[i][i]>=0:
        print('В графе есть петли')
        break

print("\n------------------------")
