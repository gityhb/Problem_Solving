import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

result = []
queue = deque()

for i in range(1, N+1):
    queue.append(i)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())

    result.append(queue.popleft())

str_result = map(str, result)
print(f"<{', '.join(str_result)}>")