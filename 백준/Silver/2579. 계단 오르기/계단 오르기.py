import sys

n = int(sys.stdin.readline())
st = [0] * (1000)

for i in range(n):
    st[i] = int(sys.stdin.readline())

dp = [-100000] * (1000)

dp[0] = st[0]
dp[1] = st[0]+st[1]
dp[2] = max(st[0], st[1]) + st[2]

for i in range(3, n):
    dp[i] = max(dp[i-2]+st[i], dp[i-3]+st[i-1]+st[i])

print(dp[n-1])