import sys
from collections import deque

T = int(sys.stdin.readline())

result = []

dx= [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(start_y, start_x, end_y, end_x):
    queue = deque()
    visited[start_y][start_x]=True
    queue.append((start_y, start_x))

    while queue:
        ty, tx = queue.popleft()

        if ty == end_y and tx == end_x:
            return graph[ty][tx]
        
        for i in range(8):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0<=nx<l and 0<=ny<l:
                if not visited[ny][nx]: 
                    graph[ny][nx] = graph[ty][tx] + 1
                    visited[ny][nx]=True
                    queue.append((ny, nx))


for _ in range(T):
    l = int(sys.stdin.readline())

    graph = [[0] * l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    start_y, start_x = map(int, sys.stdin.readline().split())
    end_y, end_x = map(int, sys.stdin.readline().split())

    k = bfs(start_y, start_x, end_y, end_x)
    result.append(k)

for i in result:
    print(i)