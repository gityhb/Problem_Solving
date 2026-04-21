import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = []

def bfs(y, x):
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))

    while queue:
        ky, kx = queue.popleft()
        for i in range(4):
            nx = kx + dx[i]
            ny = ky + dy[i]
            if 0<= nx < M and 0<=ny<N:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

for _ in range(T):

    count =  0
    M, N, K = map(int, sys.stdin.readline().split())

    visited = [[False]*M for _ in range(N)]
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j]==1:
                bfs(i, j)
                count+=1
    
    result.append(count)

for i in result:
    print(i)