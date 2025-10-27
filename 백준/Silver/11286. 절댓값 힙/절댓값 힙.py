import sys, heapq

heap = []

N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    
    elif x == 0:
        if not heap:
            print(0)
        else:
            pop_list = heapq.heappop(heap)
            print(pop_list[1])