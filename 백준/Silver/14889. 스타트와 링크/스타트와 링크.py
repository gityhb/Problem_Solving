import sys

N = int(sys.stdin.readline())
power = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
min_diff = float('inf')

def dfs(idx, count):
    global min_diff
    
    if count == N // 2:
        start_score = 0
        link_score = 0
        
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_score += power[i][j]
                elif not visited[i] and not visited[j]:
                    link_score += power[i][j]
        
        min_diff = min(min_diff, abs(start_score - link_score))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, count + 1)
            visited[i] = False

dfs(0, 0)
print(min_diff)