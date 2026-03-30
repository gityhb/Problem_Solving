from itertools import product
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = []
for i in range(1, N+1):
    numbers.append(i)

for i in product(numbers, repeat=M):
    print(*i)