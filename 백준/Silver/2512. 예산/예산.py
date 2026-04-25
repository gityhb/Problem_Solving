import sys

N = int(sys.stdin.readline())
jibang = list(map(int, sys.stdin.readline().split()))
limit = int(sys.stdin.readline())

start = 0
end = max(jibang)
result = 0 #배정된 최대 예산상한액

while start<=end:
    mid = (start+end) // 2
    total = 0
    
    for i in range(N):
        total += min(jibang[i], mid)

    if total <= limit:
        result = mid
        start = mid+1
    else: end = mid-1

print(result)