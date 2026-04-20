import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    abs = list(map(int, sys.stdin.readline().split()))
    graph.append(abs)

def bfs(start_x, start_y):
    queue = deque()
    visited[start_y][start_x] = True
    queue.append((start_y, start_x))

    while queue:
        k1 = queue.popleft()
        dx = [0, 0, 0, graph[k1[0]][k1[1]]]
        dy = [0, graph[k1[0]][k1[1]], 0, 0]

        for i in range(4):
            nx = dx[i] + k1[1]
            ny = dy[i] + k1[0]

            if nx == N-1 and ny == N-1:
                return print("HaruHaru")
            
            if nx <= N-1 and ny <= N-1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    return print("Hing")

bfs(0, 0)