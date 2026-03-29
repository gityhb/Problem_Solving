from itertools import combinations
import sys

N = int(sys.stdin.readline())
num = []
for i in range(1, N+1):
    num.append(i)

count = 0

for i in combinations(num, 2):
    count += 1

print(count*2)