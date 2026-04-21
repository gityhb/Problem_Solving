import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
big_size = 0
graph = []

for _ in range(n):
    dd = list(map(int, sys.stdin.readline().split()))
    graph.append(dd)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * m for _ in range(n)]

def bfs(y, x):
    global big_size
    size = 1
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))

    while queue:
        ky, kx = queue.popleft()
        for i in range(4):
            nx = kx + dx[i]
            ny = ky + dy[i]
            if 0<= nx <= m-1 and 0<=ny <= n-1:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    size+=1
                    queue.append((ny, nx))
        
    return size

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]==1:
            size = bfs(i, j)
            big_size = max(big_size, size)
            count += 1

print(count)
print(big_size)