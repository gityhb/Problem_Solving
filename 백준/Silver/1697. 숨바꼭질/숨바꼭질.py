import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = [0] * 100001
#visited = [False] * 100000

def bfs(start):
    queue = deque()
    #visited[start] = True
    queue.append(start)

    while queue:
        d = queue.popleft()

        if d==K:
            return print(graph[d])
        
        for next in (d-1, d+1, d*2):
            if 0<= next <= 100000:
                if not graph[next]:
                    graph[next] = graph[d]+1
                    queue.append(next)
                    
bfs(N)