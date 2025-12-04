import sys, heapq

N, E = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c)) #a->b, 비용 a
    graph[b].append((a, c)) #b->a , 비용 c

def stra(start):
    distance = [100000000] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

start, end = map(int, sys.stdin.readline().split())

dist1 = stra(1) #1번에서 출발
dist2 = stra(start) #start에서 출발
dist3 = stra(end) #end에서 출발

#1 -> start->end->N
path1 = dist1[start] + dist2[end] + dist3[N]
#1->end->start->N
path2 = dist1[end] + dist3[start] + dist2[N]

result = min(path1, path2)

if result >= 100000000:
    print(-1)
else:
    print(result)