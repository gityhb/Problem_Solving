import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
hap = [0] * (N-K+1)

for i in range(0, K):
    hap[0] += arr[i]

for i in range(1, N-K+1):
    hap[i] = hap[i-1] - arr[i-1] + arr[i+K-1]

print(max(hap))