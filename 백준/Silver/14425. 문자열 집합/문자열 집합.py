import sys

N, M = map(int, sys.stdin.readline().split())

strings = set()
find = []

for _ in range(N):
    strings.add(sys.stdin.readline())

for _ in range(M):
    find.append(sys.stdin.readline())

count = 0

for aa in find:
   if aa in strings:
        count+=1

print(count)