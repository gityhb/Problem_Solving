from itertools import combinations
import sys

N ,K= map(int, sys.stdin.readline().split())
num = []

for i in range(1, N+1):
    num.append(i)

count=0

for i in combinations(num, K):
    count+=1

print(count)