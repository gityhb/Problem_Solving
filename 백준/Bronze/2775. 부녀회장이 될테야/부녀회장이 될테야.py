import sys

T = int(sys.stdin.readline())
data = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    data[0][i] = i
    data[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        data[i][j] = data[i][j-1] + data[i-1][j]

result = []

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    result.append(data[k][n])

for i in result:
    print(i)