import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

#dfs

count = 0
visited_dfs = [False] * (N+1)
result_dfs = []

def dfs(node):
    global count
    visited_dfs[node] = True
    result_dfs.append(node)

    for neighbor in graph[node]:
        if not visited_dfs[neighbor]:
            count += 1
            dfs(neighbor)

dfs(1)

print(count)