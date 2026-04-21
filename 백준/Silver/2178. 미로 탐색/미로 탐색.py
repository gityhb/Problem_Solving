import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * M for _ in range(N)]

for _ in range(N):
    ddd = list(map(int, sys.stdin.readline().strip()))
    graph.append(ddd)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))

    while queue:
        ky, kx = queue.popleft()

        if ky == N-1 and kx == M-1:
            return print(graph[ky][kx])
        for i in range(4):
            nx = kx + dx[i]
            ny = ky + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    graph[ny][nx] = graph[ky][kx] + 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))    

bfs(0, 0)