import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
result = []

for _ in range(N):
    n = sys.stdin.readline().split()
    m = n[0]

    if m == 'push':
        queue.append(int(n[1]))
    
    elif m == 'pop':
        if not queue:
            result.append(-1)
        else:
            result.append(queue.popleft())
    
    elif m == 'size':
        result.append(len(queue))

    elif m == 'empty':
        if not queue:
            result.append(1)
        else:
            result.append(0)

    elif m == 'front':
        if not queue:
            result.append(-1)
        else:
            result.append(queue[0])
    
    elif m == 'back':
        if not queue:
            result.append(-1)
        else:
            result.append(queue[-1])

print('\n'.join(map(str, result)))