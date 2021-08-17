N=int(input()) # длинная сторона
M=int(input()) # короткая сторона
x=int(input())
y=int(input())

if N < M:
    N, M = M, N

if M - x < x:
    x = M - x

if N - y < y:
    y = N - y

if x < y:
    print(x)
else:
    print(y)