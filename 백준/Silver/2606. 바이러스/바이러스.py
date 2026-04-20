import sys
from collections import deque

num = int(sys.stdin.readline())
t = int(sys.stdin.readline())

visited = [False] * (num+1)

graph = [[] * (num+1) for _ in range(num+1)]

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True

    for next in graph[start]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

dfs(1)

print(visited.count(True)-1)