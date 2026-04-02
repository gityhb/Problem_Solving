import sys
sys.setrecursionlimit(10**6)


T = int(sys.stdin.readline()) #테스트 횟수
result = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
            
for _ in range(T):
    count = 0
    M, N, K = map(int, sys.stdin.readline().split()) #가로, 세로 길이
    graph=[[0]*M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] =1

    def dfs(x, y):
        graph[y][x] = 0

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<M and 0<=ny<N:
                if graph[ny][nx] == 1:
                    dfs(nx, ny)

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs(x, y)
                count+=1 
    
    result.append(count)

for i in result:
    print(i)