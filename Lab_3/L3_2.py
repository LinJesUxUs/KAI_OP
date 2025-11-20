from functions import randomList

print( "Лаба-3. Задание-2.10" )

def editedRandomList():
    A = randomList()
    print("Исходный список\n",*A)
    
    # Поиск группы, содержащей наибольшее число
    # подряд идущих положительных элементов
    begin = 0
    end = 0
    
    for i in range(len(A)):
        if A[i] <= 0:
            continue
        for j in range(i+1,len(A)):
            if (A[j] <= 0) or (j == len(A)-1):
                if (j-i > end-begin):
                    if (j == len(A)-1 and A[j] > 0 ):
                        end = j+1
                    else:
                        end = j
                    begin = i
                i = j
                break
    
    # Переписка группы в хвост
    A.extend(A[begin:end])
    A = A[0:begin] + A[end:]
    return A

A = editedRandomList()
print("Перегруппированный список\n",*A)
