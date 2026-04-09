import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

dfs_result = []
bfs_result = []

def dfs(node):
    dfs_visited[node] = True
    dfs_result.append(node)
    
    for next_node in graph[node]:
        if not dfs_visited[next_node]:
            dfs(next_node)

def bfs(start):
    queue = deque([start])
    bfs_visited[start] = True
    
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        
        for neighbor in graph[node]:
            if not bfs_visited[neighbor]:
                bfs_visited[neighbor] = True
                queue.append(neighbor)

dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)