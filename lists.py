# Четные индексы
list = input().split()

for i in range(0, len(list), 2):
	print(int( list[i] ), end=' ')

# Четные элементы
list = input().split()

for i in [int(x) for x in list]:
	if i % 2 == 0:
		print(i, end=' ')

# Больше предыдущего
list = input().split()
prev = 0

for i in range(len(list)):
	x = int(list[i])
	if i and x > prev:
		print(x, end=' ')
	prev = x

# Соседи одного знака
list = input().split()
prev = 0

for i in range(len(list)):
	x = int(list[i])
	if i and x * prev > 0:
		print(prev, x)
		break
	prev = x

# Больше своих соседей
list = input().split()
cnt = 0

for i in range(1, len(list) - 1):
	if list[i] > list[i - 1] and list[i] > list[i + 1]:
		cnt += 1

print(cnt)

# Наибольший элемент
list = [int(x) for x in input().split()]
maxEl = list[0]
maxElIdx = 0

for i in range(1, len(list)):
	if list[i] > maxEl:
		maxEl = list[i]
		maxElIdx = i

print(maxEl, maxElIdx)

# Шеренга
list = [int(x) for x in input().split()]
x = int(input())
n = len(list) + 1

for i in range(len(list)):
	if x > list[i]:
		n = i + 1
		break

print(n)

# Количество различных элементов
list = [int(x) for x in input().split()]
cnt = 1

for i in range(1, len(list)):
	if list[i] != list[i - 1]:
		cnt += 1

print(cnt)

# Переставить соседние
list = input().split()

for i in range(1, len(list), 2):
	list[i - 1], list[i] = list[i], list[i - 1]

print(' '.join(list))

# Переставить min и max
list = [int(x) for x in input().split()]
maxElIdx = 0
minElIdx = 0

for i in range(1, len(list)):
	if list[i] > list[maxElIdx]:
		maxElIdx = i
	if list[i] < list[minElIdx]:
		minElIdx = i

list[maxElIdx], list[minElIdx] = list[minElIdx], list[maxElIdx]

print(' '.join([str(x) for x in list]))

# Удалить элемент
list = input().split()
k = int(input())

for i in range(k + 1, len(list)):
	list[i - 1] = list[i]

list.pop()

print(' '.join(list))

# Вставить элемент
list = input().split()
list.append(0)
newEl = input().split()
k = int(newEl[0])
c = newEl[1]

for i in range(len(list) - 1, k, -1):
	list[i] = list[i - 1]

list[k] = c
print(' '.join(list))

# Количество совпадающих пар
list = input().split()
listLen = len(list)
cnt = 0

for i in range(listLen):
	for j in range(i + 1, listLen):
		if list[i] == list[j]:
			cnt += 1

print(cnt)

# Уникальные элементы
list = input().split()
listLen = len(list)
uniqList = []

for i in range(listLen):
	isUniq = True
	for j in range(listLen):
		if i != j and list[i] == list[j]:
			isUniq = False
			break

	if isUniq:
		uniqList.append(list[i])

print(' '.join(uniqList))
