#  Создайте текстовый файл in.txt, в который поместите текст
# (объёмом примерно 0,5 страницы). Затем ваша программа должна считать
# данные из файла, выполнить операции в соответствии с вариантом. Результат
# нужно записать в текстовый файл out.txt.

# 10. Удалить последовательности символов, заключённе в фигурные скобки

import os
print("Лаба-5. Задание-5.1")

def getRecursCloseBraceIndex (text: str, begin_char, end_char):
	# Поиск закрывающего символа, с учётом вложений
	length = -1
	count = 0
	for i in text:
		length += 1
		if i == begin_char: count += 1 # найден открывающий символ, +1 вложенности
		elif i == end_char: count -= 1 # найден закрывающий символ, -1 вложенности
		if count == 0: break
	return length

f = open( os.path.dirname(os.path.abspath(__file__)) + "/in.txt", 'r', encoding='utf-8')
text = f.read()
begin_char = '{'
end_char = '}'

while(True):
	begin = text.find(begin_char) # индекс первого открывающего символа
	if begin < 0: break # больше нет открывающих символов
	end = begin + getRecursCloseBraceIndex(text[begin:], begin_char, end_char)
	text = text[:begin] + text[end+1:]

f.close()
f = open( os.path.dirname(os.path.abspath(__file__)) + "/out.txt", 'w', encoding='utf-8')
f.write(text)
# print(text)

f.close()
