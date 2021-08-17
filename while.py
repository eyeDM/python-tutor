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
