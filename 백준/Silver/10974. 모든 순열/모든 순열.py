import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr=[]
for i in range(1, N+1):
    arr.append(i)

for i in permutations(arr):
    print(*i)