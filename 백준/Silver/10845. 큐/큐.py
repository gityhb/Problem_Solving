import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    
    op = command[0]
    
    if op == "push":
        queue.append(command[1])
        
    elif op == "pop":
        if not queue:
            print("-1")
        else:
            print(queue.popleft())
            
    elif op == "size":
        print(len(queue))
        
    elif op == "empty":
        print(1 if not queue else 0)
        
    elif op == "front":
        if not queue:
            print("-1")
        else:
            print(queue[0])
            
    elif op == "back":
        if not queue:
            print("-1")
        else:
            print(queue[-1])