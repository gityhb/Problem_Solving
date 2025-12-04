import sys, heapq

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
distance = [300000] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1)) #a->b 거리는 1고정

def stra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)
    
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

stra(X)

answer = []
for i in range(1, N+1):
    if distance[i] == K:
       answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)