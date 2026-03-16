import sys

N, M = map(int, sys.stdin.readline().split())

numbers = [0] * (N+1)

for i in range(1, N+1):
    numbers[i] = i

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b]=temp

print(*numbers[1:])