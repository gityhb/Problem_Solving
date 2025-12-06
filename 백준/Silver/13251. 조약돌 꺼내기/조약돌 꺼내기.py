import sys, math

M = int(sys.stdin.readline())
color = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

hap = sum(color)
b= math.comb(hap, K)
a=0

for i in range(M):
    a += math.comb(color[i], K)

print(a/b)