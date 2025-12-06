import sys, math

N, K = map(int, sys.stdin.readline().split())

print((math.comb(N, K))%10007)