from itertools import combinations
import sys

N = int(sys.stdin.readline())
result=1

if N==0:
    print(1)
else:
    for i in range(N, 1, -1):
        result *= i
    print(result)