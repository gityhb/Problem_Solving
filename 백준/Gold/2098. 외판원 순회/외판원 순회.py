import sys

input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited):
    if visited == (1 << N) - 1:
        if W[now][0] > 0:
            return W[now][0]
        else:
            return INF

    if dp[now][visited] != -1:
        return dp[now][visited]

    min_cost = INF
    
    for next_city in range(N):
        if not (visited & (1 << next_city)) and W[now][next_city] > 0:
            cost = dfs(next_city, visited | (1 << next_city)) + W[now][next_city]
            min_cost = min(min_cost, cost)

    dp[now][visited] = min_cost
    return min_cost

print(dfs(0, 1))