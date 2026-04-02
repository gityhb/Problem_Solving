import sys
sys.setrecursionlimit(10**6)

N, M ,R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

count=1
visited = [0] * (N+1)

def dfs(node):
    global count
    visited[node] = count
    count += 1

    for next in graph[node]:
        if visited[next] == 0:
            dfs(next)

dfs(R)

for i in range(1, N+1):
    print(visited[i])