import sys
from collections import deque

com = int(sys.stdin.readline())
line = int(sys.stdin.readline())

graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)

for _ in range(line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    num = 0
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        d = queue.popleft()
        for next in graph[d]:
            if not visited[next]:
                num += 1
                visited[next] = True
                queue.append(next)
     
    return num

print(bfs(1))