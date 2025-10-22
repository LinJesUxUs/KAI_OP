import math

R1 = int(input("Введите больший радиус \'R1\' "));
print("Введён радиус \'R1\' = ", R1);
R2 = int(input("Введите миньший радиус \'R2\' "));
print("Введён радиус \'R2\' = ", R2);

if R1 < R2: print("Радиусы введены не правильном порядке, но я всё решу");
def circle_square(rad):
	return math.pi * (rad ** 2)

print("Площадь кольца = ", math.fabs(circle_square(R1)-circle_square(R2)) );
