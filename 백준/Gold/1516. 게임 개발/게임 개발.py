from collections import deque
import sys

N = int(sys.stdin.readline())

time = [0] * (N+1)
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
result = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, sys.stdin.readline().split()))
    
    time[i] = data[0]

    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i) 
        result[i] = time[i]

while q:
    now = q.popleft()
    
    for next_node in graph[now]:
        indegree[next_node] -= 1

        #max(기존 계산값, 이전건물완료시간 + 내건물건설시간)
        result[next_node] = max(result[next_node], result[now] + time[next_node])
        
        if indegree[next_node] == 0:
            q.append(next_node)

for i in range(1, N+1):
    print(result[i])