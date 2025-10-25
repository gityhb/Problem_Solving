import sys

N = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))

M = max(scores)
sum = 0

for i in range(N):
    scores[i] = scores[i]/M*100
    sum += scores[i]

print(sum/N)