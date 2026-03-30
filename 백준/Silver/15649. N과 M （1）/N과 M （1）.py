from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = []
for i in range(1, N+1):
    numbers.append(i)

for i in permutations(numbers, M):
    print(*i)