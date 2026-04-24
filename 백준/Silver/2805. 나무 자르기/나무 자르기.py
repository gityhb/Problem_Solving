import sys

N, K = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0 
end = max(tree)

result = 0 

while start <= end:
    mid = (start + end) // 2
    
    hap = 0
    for t in tree:
        if t > mid:
            hap += t - mid
            
    if hap >= K: 
        result = mid
        start = mid + 1
        
    elif hap < K:
        end = mid - 1


print(result)