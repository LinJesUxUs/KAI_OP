A = int(input("Введите число A "))
if (A < 1000) & (A > 99) :
    hig = A // 100
    med = A // 10 % 10
    low = A % 10
    print( hig + (med*10) + (low*100) )
else :
	print("Не трёхзначное число")