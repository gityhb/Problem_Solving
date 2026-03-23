import sys

N = int(sys.stdin.readline())
numbers= []

for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))

    numbers.append(num[::-1])

numbers.sort()

for i, j in numbers:
    print(j, i)