import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True) #큰순으로 정렬

count = 0

for coin in coins:
    if K==0: break
    if K>=coin:
        count = K//coin + count
        K = K%coin


print(count)