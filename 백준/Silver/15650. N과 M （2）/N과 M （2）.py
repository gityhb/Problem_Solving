from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = []
for i in range(1, N+1):
    numbers.append(i)

for i in combinations(numbers, M):
    print(*i)