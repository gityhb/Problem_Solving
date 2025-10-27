import sys
from collections import deque

N, M, V = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

#dfs
visited_dfs = [False] * (N+1)
dfs_result = []

def dfs(node):
    visited_dfs[node] = True
    dfs_result.append(node) #방문노드 기록

    for neighbor in graph[node]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

#bfs
visited_bfs = [False] * (N+1)
bfs_result = []

def bfs(start_node):
    queue = deque([start_node])

    visited_bfs[start_node] = True
    while queue:
        node = queue.popleft()
        bfs_result.append(node)

        for neighbor in graph[node]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)

dfs(V)
bfs(V)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))