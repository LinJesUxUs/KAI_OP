from typing import Final
import random

print( "Лаба-3. Задание-2.10" )

INT_MAX: Final = int(2**8/2-1)
INT_MIN: Final = int(-2**8/2)

n = int(0)
A = []

# Обработка ввода колличества случайных переменных
def customRand(error: bool = False):
    global n
    if error:
        print("Колличество будет определено случайно!")
        n = random.randint(1,INT_MAX)
    else: return random.randint(INT_MIN,INT_MAX)

try:
    n = int(input("Введите колличество случайных переменных:\n"))
    if n == 0:
        raise
except ValueError:
    print("Введено не целочисленное число")
    customRand(True)
except:
    print("Введён 'n' равный 0")
    customRand(True)

if n < 0 :
    print("Введено отрицительное число. Беру его по модулю")
    n = abs(n)

# Заполнение случайными переменными
for i in range(n):
    A.append(customRand())

max_length = 0
current_length = 0
begin = 0
end = 0
finish = False

while !finish:
    while (arr[end] > 0):
    else: arr


for i in range(len(arr)):
    if arr[i] > 0:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0

print(n,A)
