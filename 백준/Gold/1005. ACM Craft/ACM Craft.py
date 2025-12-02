import sys
from collections import deque

T = int(sys.stdin.readline())

dap = [0] * T

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())

    time = [0] + list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    result = [0] * (N+1)

    for i in range(1, K+1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1

    W = int(sys.stdin.readline())

    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = time[i]
        
    while q:
        now = q.popleft()

        for next_node in graph[now]:
            indegree[next_node] -= 1
            result[next_node] = max(result[next_node], result[now]+time[next_node])

            if indegree[next_node]==0:
                q.append(next_node)

    print(result[W])