import sys

T = int(sys.stdin.readline())

result = []
times = [300, 60, 10]

for time in times:
    result.append(T//time)
    T = T % time

if T == 0:
    print(*result)
else: print(-1)