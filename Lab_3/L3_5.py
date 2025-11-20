from functions import getUIntWithMsg
from typing import Final
import random

ROWS: Final = getUIntWithMsg("Введите колличество строк матрицы.\n"
							,"Введено не целое число!")

COLS: Final = getUIntWithMsg("Введите колличество столбцов матрицы.\n"
							,"Введено не целое число!")

val = getUIntWithMsg("Введите число для поиска.\n"
					,"Введено не целое число!")

col = 0
row = 0
mult = 0

# Создание и инициализация матрицы
A = [ [ random.randint(1, int(2**8/2-1))
		for i in range(COLS)]
		for i in range(ROWS)]

# Поиск элемента
for i in A:
	print(i)
	if mult <= 0:
		for j in i:
			if (j % val) == 0:
				col = i.index(j)
				row = A.index(i)
				mult = int(j / val)
				val = j
				break

if mult != 0:
	print("Элемент:",val,
		"\nИндекс:",row,col,
		"\nКратность:",mult )
else: print("Элемент кратный",val,"не найден")