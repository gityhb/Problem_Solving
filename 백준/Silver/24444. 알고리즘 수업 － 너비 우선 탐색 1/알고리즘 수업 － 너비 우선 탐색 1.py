import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

#오른차순으로 방문
for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    count = 1
    visited[start] = count

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                count += 1
                visited[neighbor] = count
                queue.append(neighbor)
        
bfs(R)

for i in range(1, N+1):
    print(visited[i])