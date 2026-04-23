import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

hap = [times[0]] * N
result = [times[0]] * N

for i in range(1, N):
    hap[i] = hap[i-1] + times[i]
    result[i] = result[i-1] + hap[i]

print(result[N-1])