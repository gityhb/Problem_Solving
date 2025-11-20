import sys

def find(a):
    if parent[a] == a:
        return a
    
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA


N = int(sys.stdin.readline()) #총 도시 수
M = int(sys.stdin.readline()) #여행 갈 도시 수

parent = [i for i in range(N+1)]

for i in range(N):
    link_info = list(map(int, sys.stdin.readline().split()))

    for j in range(N):
        if link_info[j] == 1: #1이면 연결
            union(i+1, j+1)

plan = list(map(int, sys.stdin.readline().split()))

start_root = find(plan[0])
possible = True

for i in range(1, len(plan)):
    if find(plan[i]) != start_root:
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")