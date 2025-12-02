from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    singers = data[1:]

    for j in range(len(singers)-1):
        a = singers[j]
        b = singers[j+1]
        graph[a].append(b)
        indegree[b] += 1

result = []
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for next_node in graph[now]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)