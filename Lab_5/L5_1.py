#  Создайте текстовый файл in.txt, в который поместите текст
# (объёмом примерно 0,5 страницы). Затем ваша программа должна считать
# данные из файла, выполнить операции в соответствии с вариантом. Результат
# нужно записать в текстовый файл out.txt.

# 10. Удалить последовательности символов, заключённе в фигурные скобки

print("Лаба-5. Задание-5.1")

def getRecursCloseBraceIndex (s: str, bc, ec):
	length = -1
	count = 0
	for i in s:
		length += 1
		if i == bc: count += 1
		elif i == ec: count -= 1
		if count == 0: break
	return length

f = open("in.txt")
text = f.read()
bc = '{'
ec = '}'

while(True):
	begin = text.find(bc)
	if begin < 0: break
	end = begin + getRecursCloseBraceIndex(text[begin:],bc,ec)
	text = text[:begin] + text[end+1:]

print(text)

f.close()
