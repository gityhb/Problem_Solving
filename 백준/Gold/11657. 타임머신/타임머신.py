import sys

N, M = map(int, sys.stdin.readline().split())

edge = []
min = [float('inf')] * (N+1)

for _ in range(M):
    a, b, c= map(int, sys.stdin.readline().split())

    edge.append((a, b, c))

def bellman(start):
    min[start] = 0

    for i in range(N):

        for u, v, t in edge:
            if min[u] != float('inf') and min[v] > min[u] + t:
                min[v] = min[u]+t

                if i == N-1:
                    return True

    return False
 
nega = bellman(1)

if nega:
    print(-1)
else:
    for i in range(2, N+1):
        if min[i] == float('inf'):
            print(-1)
        else:
            print(min[i])