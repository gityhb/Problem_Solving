import sys, heapq

N = int(sys.stdin.readline()) #도시 개수
M = int(sys.stdin.readline()) #버스 개수(간선)

graph = [[] for _ in range(N+1)]
distance = [100000000] * (N+1) #최대 버스 비용으로 초기화

for _ in range(M):
    a, b, c= map(int, sys.stdin.readline().split())
    graph[a].append((b, c)) #a->b에 드는 비용 c

def stra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, sys.stdin.readline().split())
stra(start)
print(distance[end])