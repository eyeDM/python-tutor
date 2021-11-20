import math

# Длина отрезка
def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print( distance(x1, y1, x2, y2) )

# Отрицательная степень
def __positivePower(a, n):
	res = 1
	for i in (range(n)):
		res *= a
	return res

def power(a, n):
	if n > 0:
		return __positivePower(a, n)
	elif n < 0:
		return __positivePower(1/a, -n)
	else:
		return 1

a = float(input())
n = int(input())

print( power(a, n) )

# Большие буквы
def capitalize(str):
	result = []
	for word in str.split():
		firstLetter = word[0]
		firstLetter = chr(ord(firstLetter) - 32)
		result.append(firstLetter + word[1:])

	return ' '.join(result)

print( capitalize(input()) )

# Возведение в степень
def __powerReq(a, n, result):
	if n == 0:
		return 1
	if n == 1:
		return result
	return __powerReq(a, n - 1, result*a)

def power(a, n):
	return __powerReq(a, n, a)

a = float(input())
n = int(input())
print( power(a, n) )

# (-) Разворот последовательности
str = ''
i = 1
while i != '0':
	i = input()
	str = i + ' ' + str

str = '0' + ' ' + str
for n in str.split():
	print(n)

# Числа Фибоначчи
def __feb(n, i_1, i_2):
	if n < 2:
		return i_1
	i = i_1 + i_2
	return __feb(n - 1, i, i_1)

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return __feb(n, 1, 0)

print( fib(int(input())) )
