from collections import deque
import sys

N = int(sys.stdin.readline())

#그래프 완성(양방향)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1) #부모 저장 ex) parent[3] = 1은 3의 부모가 1이라는 것.
depth = [0] * (N+1) #깊이 저장
visited = [False] * (N+1) #방문 여부

def bfs(root):
    #큐 대기열을 만들고 루트 노드를 넣음
    q = deque([root])

    #루트 노드 정보 기록
    visited[root] = True #1번 방문 체크 완료
    depth[root] = 0 #루트는 0번 (최상위) 깊이

    #큐가 빌 때까지..
    while q:
        now = q.popleft() #대기열 맨앞 꺼냄 ex)부모

        #꺼낸 노드와 연결된 모든 노드를 봄
        for child in graph[now]:
            #방문하지 않음 -> 내 자식
            if not visited[child]:
                #방문 체크!
                visited[child] = True
                #child의 부모는 now 현재 값이야!
                parent[child] = now
                #깊이는 부모보다 1층 더 깊다!
                depth[child] = depth[now] +1
                #이제 큐에 집어넣고 child를 기준으로 한번 더 돌자
                q.append(child)

def lca(a, b):
    #b가 더 깊도록 바꿈
    if depth[a] > depth[b]:
        a, b = b, a

    #a와 b가 같은 깊이 될때까지 부모님 호출
    while depth[a] != depth[b]:
        b = parent[b]

    #같은 층인데 다른 노드라면 (공통 조상 x)
    while a != b:
        a = parent[a] #한층 위로
        b = parent[b] #한층 위로
    
    return a

bfs(1)

M = int(sys.stdin.readline())

for _ in range(M):
    c, d = map(int, sys.stdin.readline().split())
    print(lca(c, d))