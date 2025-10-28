import sys
import math
N, K = map(int, sys.stdin.readline().split())
Prime = [] * (N+1)

is_Prime = [True] * (N+1)
is_Prime[0] = is_Prime[1] = False

count = 0
for i in range(2, N+1):
    if is_Prime[i]:
        for j in range(i, N+1, i):
            if is_Prime[j]:
                is_Prime[j] = False
                count += 1

                if count==K:
                    print(j)
                    break