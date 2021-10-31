# Список квадратов
N = int(input())
i = 1
q = i ** 2

while q <= N:
	print(q, end=' ')
	i += 1
	q = i ** 2

# Минимальный делитель
N = int(input())
i = 2

while i <= N:
	if N % i == 0:
		print(i)
		break
	i += 1

# Степень двойки
N = int(input())
x = 2
e = 0
p = 1

while p * x <= N:
	e += 1
	p *= x
else:
	print(e, p)

# Утренняя пробежка
x = int(input())
y = int(input())

S = x
day = 1
m = 1.1

while S < y:
	day += 1
	S *= m

print(day)

# Длина последовательности
n = 0

while int(input()) != 0:
	n += 1

print(n)

# Сумма последовательности
sum = 0
x = 1

while x != 0:
	x = int(input())
	sum += x

print(sum)

# Среднее значение последовательности
sum = 0
n = 0
x = int(input())

while x != 0:
	sum += x
	n += 1
	x = int(input())

print(sum / n)

# Максимум последовательности
max = 0
x = 1

while x != 0:
	x = int(input())
	if x > max:
		max = x

print(max)

# Индекс максимума последовательности
x = 1
i = 0
maxValue = 0
maxValueIdx = 0

while x != 0:
	x = int(input())
	if x > maxValue:
		maxValue = x
		maxValueIdx = i
	i += 1

print(maxValueIdx)

# Количество четных элементов последовательности
n = 0
x = 1

while True:
	x = int(input())
	if x == 0:
		break
	if x % 2 == 0:
		n += 1

print(n)

# Количество элементов, которые больше предыдущего
n = 0
x = 1
xPrev = 0

while x != 0:
	x = int(input())
	if xPrev != 0 and x > xPrev:
		n += 1
	xPrev = x

print(n)

# Второй максимум
max = 0
max2 = 0
x = 1

while x != 0:
	x = int(input())
	if x > max:
		max2 = max
		max = x
	elif x > max2:
		max2 = x

print(max2)

# Количество элементов, равных максимуму
n = 1
max = 0
x = 1

while x != 0:
	x = int(input())
	if x > max:
		max = x
		n = 1
	elif x == max:
		n += 1

print(n)

# Числа Фибоначчи
n = int(input())
Fn = 0
Fnext = 1

for i in range(n):
	Fn, Fnext = Fnext, Fnext + Fn

print(Fn)

# Номер числа Фибоначчи
A = int(input())
n = -1
F = 0
Fnext = 1
i = 0

while True:
	if A < F:
		break

	if A == F:
		n = i
		break

	F, Fnext = Fnext, Fnext + F
	i += 1

print(n)

# Максимальное число идущих подряд равных элементов
n = 1
nMax = 1
x = 1
xPrev = 0

while True:
	x = int(input())
	if x == 0:
		break

	if x == xPrev:
		n += 1
		if n > nMax:
			nMax = n
	else:
		n = 1

	xPrev = x

print(nMax)

# Стандартное отклонение
data = []
n = 0
sum = 0

while True:
	x = int(input())
	if x == 0:
		break

	data.append(x)
	n += 1
	sum += x

mean = sum / n
qSum = 0

for x in data:
	qSum += (x - mean) ** 2

stddev = (qSum / (n - 1)) ** 0.5

print(stddev)
