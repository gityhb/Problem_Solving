import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
count = 0

def dfs(node):
    global count
    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            count+=1
            dfs(next)
    
dfs(1)

print(count)