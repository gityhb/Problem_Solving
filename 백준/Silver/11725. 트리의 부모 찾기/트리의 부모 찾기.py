import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque([1])

    parent[1] = 1 #역주행 방지

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if parent[next_node] == 0:
                parent[next_node] = now
                queue.append(next_node)

bfs()

for i in range(2, N+1):
    print(parent[i])