from itertools import combinations_with_replacement
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = []
for i in range(1, N+1):
    numbers.append(i)

for i in combinations_with_replacement(numbers, M):
    print(*i)