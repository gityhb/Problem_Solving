import sys
import heapq

heap = []
result = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if not heap:
            result.append(0)
        else:
            a = heapq.heappop(heap)
            result.append(a[1])
    
    else:
        heapq.heappush(heap, (-num, num))
    
for i in result:
    print(i)