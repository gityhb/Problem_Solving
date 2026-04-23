import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
count = 0

for _ in range(N):
    d = int(sys.stdin.readline())
    coins.append(d)

for i in reversed(range(N)):
    if coins[i] <= K:
        count += (K//coins[i])
        K = K % coins[i]
    if K == 0:
        print(count)
        break