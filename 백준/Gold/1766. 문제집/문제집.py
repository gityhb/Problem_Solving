import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) #a->b
    indegree[b] += 1 #진입차수 1개 증가

result = []
q = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i) #데이터 넣을 때 자동으로 정렬, 작은 값 맨 앞으로

while q:
    now = heapq.heappop(q) #가장 번호 작은 문제 꺼냄
    result.append(now) 

    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] ==0:
            heapq.heappush(q, next)

print(*result)