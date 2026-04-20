import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []

for _ in range(N):
    dd = sys.stdin.readline().strip()
    graph.append(list(dd))


visited = [[False]*M for _ in range(N)]


def bfs(y, x):
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))

    shape=graph[y][x]

    while queue:
        cy, cx = queue.popleft()
        
        if shape == '-':
            ny = cy
            nx = cx + 1
            if nx < M and not visited[ny][nx] and graph[ny][nx] == '-':
                visited[ny][nx] = True
                queue.append((ny, nx))
        
        elif shape == '|':
            ny = cy+1
            nx = cx
            if ny < N and not visited[ny][nx] and graph[ny][nx] == '|':
                visited[ny][nx] = True
                queue.append((ny, nx))

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)