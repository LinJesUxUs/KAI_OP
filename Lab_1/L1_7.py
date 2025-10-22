A = int(input("Введите число A "));
if (A < 1000) & (A > 99) :
    hig = A // 100;
    med = A // 10 % 10;
    low = A % 10;
    print( ( A - (hig*100) ) * 10 + hig )
else :
	print("Не трёхзначное число")