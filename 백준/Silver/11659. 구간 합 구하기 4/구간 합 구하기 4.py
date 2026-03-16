import sys

N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

result = []

hap = [0]*(N+1)

for i in range(1, N+1):
    hap[i] = hap[i-1]+numbers[i-1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    result.append(hap[b]-hap[a-1])

for i in result:
    print(i)