import sys

N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

count = 0

def dfs(idx, current_sum):
    global count
    if idx >= N:
        return

    current_sum += nums[idx]

    if current_sum == S:
        count+=1

    dfs(idx+1, current_sum)
    dfs(idx+1, current_sum-nums[idx])

dfs(0, 0)

print(count)