import sys

N, M = map(int, sys.stdin.readline().split())

numbers = [0] * (N+1)

for i in range(1, N+1):
    numbers[i] = i

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    for i in range(int((b-a+1)/2)):
        numbers[a+i], numbers[b-i] = numbers[b-i], numbers[a+i]

print(*numbers[1:])