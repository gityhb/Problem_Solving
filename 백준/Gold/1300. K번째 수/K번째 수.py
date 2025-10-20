import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
ans = 0

while start <= end:
    middle = (start+end) // 2

    count = 0

    for i in range(1, N+1):
        count += min(N, middle // i)

    if count >= k:
        ans = middle
        end = middle - 1
    
    else:
        start = middle + 1

print(ans)