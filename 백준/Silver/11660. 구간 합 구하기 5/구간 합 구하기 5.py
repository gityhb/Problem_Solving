import sys

N, M = map(int, sys.stdin.readline().split())

A = [[0] * (N+1) for _ in range(N+1)]
D = [[0] * (N+1) for _ in range(N+1)]
results = [0] * M

for i in range(1, N+1):
    numbers = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N+1): 
        A[i][j] = numbers[j-1]
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

for m in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    results[m] = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]

for i in range(M):
    print(results[i])