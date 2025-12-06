import sys, math

T = int(sys.stdin.readline())

result = []

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    result.append(math.comb(M, N))

for i in result:
    print(i)