from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

indegree = [0] * (N+1) #모든 노드 진입차수 0으로 초기화

graph = [[] for i in range(N+1)] #각 노드 연결된 간선정보 담기위한 그래프

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()