import math

print( "Лаба-2. Задание-2" )

phrase = ""
while True:
    phrase = input("Введите любую любую фразу от 10 символов:\n")
    if (len(phrase) >= 10 ):
        break

print( "а) ", phrase[ :4] )
print( "б) ", phrase[-4: ] )

phraseMid = len(phrase)//2
if (len(phrase)%2 > 0):
    print( "в) ", phrase[ phraseMid ] )
else:
    print( "в) ", phrase[ phraseMid-1: phraseMid+1 ] )
print( "г) ", phrase[3:8+1] )
#print( "г) ", phrase[3-1:8] )
