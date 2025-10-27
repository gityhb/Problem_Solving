import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False] * (N+1)

def dfs(node):
    global possible
    visited_dfs[node] = True

    for neighbor in graph[node]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

component_count = 0

for i in range(1, N + 1):
    if not visited_dfs[i]:
        component_count += 1
        dfs(i)

print(component_count)