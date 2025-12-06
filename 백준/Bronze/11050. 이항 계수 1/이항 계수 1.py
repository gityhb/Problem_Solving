import sys

N, K = map(int, sys.stdin.readline().split())

data = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    data[i][1] = i
    data[i][i] = 1
    data[i][0] = 1

for i in range(2, N+1):
    for j in range(1, i):
        data[i][j] = data[i-1][j-1]+data[i-1][j]

print(data[N][K])