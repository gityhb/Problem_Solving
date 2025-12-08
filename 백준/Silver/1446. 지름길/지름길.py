import sys, heapq

N, D = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(D+1)]
min = [float('inf')] * (D+1)

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if b>D:
        continue
    graph[a].append((b, c)) #도착지, 가는 거리

for i in range(D):
    graph[i].append((i+1, 1))

def stra(start):
    q = []
    heapq.heappush(q, (0, start)) #가는 거리 적은 것부터 나열
    min[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > min[now]:
            continue
        
        for next_node, next_dist in graph[now]:
            cost = dist + next_dist #지금까지온 거리+갈 거리
            if cost < min[next_node]:
                min[next_node] = cost #최솟값 업데이트!
                heapq.heappush(q, (cost, next_node))
    
    return min[D]

print(stra(0))