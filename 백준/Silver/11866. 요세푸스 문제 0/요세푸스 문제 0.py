import sys
from collections import deque

queue = deque()

N, K = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    queue.append(i)

result = []

while(len(queue)>=1):
    for _ in range(K-1):
        a = queue.popleft()
        queue.append(a)
    b=queue.popleft()
    result.append(b)

print("<" + ", ".join(map(str, result)) + ">")