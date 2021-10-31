N = int(input())
S = 0

for i in range(1, N + 1):
	S += i

for j in range(N - 1):
	S -= int(input())

print(S)
