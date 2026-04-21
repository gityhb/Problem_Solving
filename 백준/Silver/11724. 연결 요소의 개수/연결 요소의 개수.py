import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited =[False] * (N+1)


def dfs(start):
    for next in graph[start]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        visited[i] = True
        count+=1
        dfs(i)

print(count)