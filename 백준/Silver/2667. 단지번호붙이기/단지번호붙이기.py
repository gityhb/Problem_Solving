import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    d = list(map(int, sys.stdin.readline().strip()))
    graph.append(d)

visited = [[False] * (N) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = []

def bfs(y, x):
    num = 1 #단지수 세기
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))

    while queue:
        ky, kx = queue.popleft()
        for i in range(4):
            nx = dx[i] + kx
            ny = dy[i] + ky
            if 0<=nx<N and 0<=ny<N and graph[ny][nx] == 1:
                if not visited[ny][nx]:
                    num+=1
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    
    return num

home = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            home += 1
            result.append(bfs(i, j))

print(home)
result.sort()
for i in result:
    print(i)