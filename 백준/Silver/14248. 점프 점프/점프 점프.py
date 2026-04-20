import sys
from collections import deque

n = int(sys.stdin.readline())
rocks = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline())

visited = [False] * n

def bfs(start):
    queue = deque()
    visited[start-1] = True
    queue.append(start-1)

    while queue:
        f = queue.popleft()

        k1 = f-rocks[f]
        k2 = f+rocks[f]

        if 0<= k1 <= n-1:
            if not visited[k1]:
                visited[k1] = True
                queue.append(k1)
        
        if 0<=k2<=n-1:
            if not visited[k2]:
                visited[k2] = True
                queue.append(k2)

bfs(start)

print(visited.count(True))