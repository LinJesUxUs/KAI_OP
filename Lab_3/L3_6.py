from functions import getUIntWithMsg
from typing import Final
import random

ROWS: Final = 3
COLS: Final = 5
DEPT: Final = 7
row = 0
col = 0
dep = 0
maxVal = 0

# Создание и инициализация матрицы
A = [[[ random.randint(1, int(2**8/2-1))
		for i in range(DEPT)]
		for i in range(COLS)]
		for i in range(ROWS)]

# Поиск элемента
for i in A:
	for j in i:
		print(j)
		for k in j:
			if k > maxVal:
				row = A.index(i)
				col = i.index(j)
				dep = j.index(k)
				maxVal = k
	print("")

print("Элемент:", maxVal, "\nИндекс:", row, col, dep)
