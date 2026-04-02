import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
count = 0

def dfs(node):
    visited[node] = True
    
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)