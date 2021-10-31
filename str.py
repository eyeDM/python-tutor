s = input()
l = len(s)    # длина строки
#

# Делаем срезы
r = s[2]      # третий символ
r = s[-2:-1]  # предпоследний символ
r = s[:5]     # первые пять символов
r = s[:-2]    # без последних двух символов
r = s[0::2]   # все символы с четными индексами
r = s[1::2]   # символы с нечетными индексами
r = s[::-1]   # все символы строки в обратном порядке
r = s[::-2]   # все символы строки через один в обратном порядке, начиная с последнего


# Количество слов
r = s.count(' ') + 1

# Две половинки
l1 = l // 2 + l % 2
r = s[l1:] + s[:l1]

# Переставить два слова
spacePos = s.find(' ')
r = s[spacePos + 1:], s[:spacePos]

# Первое и последнее вхождения
needle = 'f'
fPos = s.find(needle)
if fPos != -1:
	lPos = s.rfind(needle)
	if lPos != fPos:
		r = str(fPos) + ' ' + str(lPos)
	else:
		r = fPos

# Второе вхождение
needle = 'f'
fPos = s.find(needle)
if fPos == -1:
	r = -2
else:
	sPos = s[fPos + 1:].find(needle)
	if sPos != -1:
		r = sPos + fPos + 1
	else:
		r = -1

# Удаление фрагмента
needle = 'h'
fPos = s.find(needle)
lPos = s.rfind(needle)
r = s[:fPos] + '#' + s[lPos + 1:]

# Обращение фрагмента
needle = 'h'
fPos = s.find(needle)
lPos = s.rfind(needle)
r = s[:fPos + 1] + s[lPos - 1:fPos:-1] + s[lPos + 1:]

# Замена подстроки
r = s.replace('1', 'one')

# Удаление символа
r = s.replace('@', '')

# Замена внутри фрагмента
needle = 'h'
fPos = s.find(needle)
lPos = s.rfind(needle)
r = s[:fPos + 1] + s[fPos + 1:lPos].replace(needle, 'H') + s[lPos:]

# Удалить каждый третий символ
step = 3
r = ''
for i in range(0, l, step):
	r += s[i + 1:i + step]

#
print(r)
