import math

def double_chars(s_):
    buf = ""
    for c in s_:
        if (c == ' '):
            buf += c
        else:
            buf += c * 2
    return buf

print( "Лаба-3. Задание-1" )

s = [""] #объявление пустого листа
while True:
    s = input(
        "Введите строку заканчивающуюся точкой:\n")
    
    if (s[-1] != "." ):
        print("Строка не заканчивается точкой!")
        continueX
    break

lst = s[:-1].split(" ")

print( "а)", len(s)-1 )
print( "б)", len(lst) )
print( "в) кротчайшее:", min(lst, key=len),
          "длиннейшее:", max(lst, key=len) )
print( "г)", double_chars(s[:-1].replace("*","")) )
