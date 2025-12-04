import sys, heapq

INF = int(1e9)
V, E = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline()) #시작 정점의 번호

graph = [ [] for _ in range(V+1)]
distance = [INF] * (V+1)

for i in range(1, E+1):
    u, v, w= map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = [] #시작 노드로 가기위한 최단경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start)) #(거리, 노드) 형태로 저장. 거리가 우선순위 기준
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) #최단거리 짧은 노드 정보 꺼냄

        if distance[now] < dist:
            continue #현 노드가 이미 처리됐으면 무시 (꺼낸거리 현 기록거리보다 길면 안 봄)

        for i in graph[now]:
            cost = dist+i[1] #i[0]:인접 노드번호, i[1]: 그 노드로 가는 비용

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])