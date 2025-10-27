import sys
import heapq

heap=[]
N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, x)
    
    else:
        if not heap: 
            print(0)
        else:
            print(heapq.heappop(heap))