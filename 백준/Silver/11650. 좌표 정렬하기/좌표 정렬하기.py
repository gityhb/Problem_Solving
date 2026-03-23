import sys

N = int(sys.stdin.readline())
numbers= []

for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))

    numbers.append(num)

numbers.sort()

for i in numbers:
    print(*i)