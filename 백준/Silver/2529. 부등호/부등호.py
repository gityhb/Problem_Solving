import sys

k = int(sys.stdin.readline())
bu = sys.stdin.readline().split()

result = []
visited = [False] * 10

def check(a, b, bu):
    if bu == '<':
        return a<b
    else: return a>b

def dfs(count, nums):
    if count == k+1:
        result.append(nums)
        return

    for i in range(10):
        if not visited[i]:
            if count==0 or check(nums[-1], str(i), bu[count-1]):
                
                visited[i] = True
                dfs(count+1, nums+str(i))
                visited[i] = False

dfs(0, "")
print(result[-1])
print(result[0])