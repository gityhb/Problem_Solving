import sys

N, M = map(int, sys.stdin.readline().split())

strings=set()
find = []

for _ in range(N):
    s = sys.stdin.readline().strip()
    strings.add(s)

for _ in range(M):
    s = sys.stdin.readline().strip()
    find.append(s)

count = 0

for s in find:
    if s in strings:
        count+=1
    
print(count)