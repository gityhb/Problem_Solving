import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [-1000000] * n
dp[0] = numbers[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])

print(max(dp))