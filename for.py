N = int(input())
S = 0

for i in range(N + 1):
	S += i

for i in range(1, N):
	S -= int(input())

print(S)
