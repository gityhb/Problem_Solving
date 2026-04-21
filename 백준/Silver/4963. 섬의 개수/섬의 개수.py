import sys
from collections import deque

result = []
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def bfs(y, x):
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))

    while queue:
        ky, kx = queue.popleft()
        for i in range(8):
            nx = kx+dx[i]
            ny = ky+dy[i]
            if 0<=nx<w and 0<=ny<h:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

while(True):
    count = 0
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    graph = []
    visited = [[False] * w for _ in range(h)]

    for _ in range(h):
        kk = list(map(int, sys.stdin.readline().split()))
        graph.append(kk)

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i, j)
                count+=1
    
    result.append(count)

for i in result:
    print(i)