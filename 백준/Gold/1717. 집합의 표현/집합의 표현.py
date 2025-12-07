import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)] #부모 배열

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a1 = find(a) #a의 부모 반환
    b1 = find(b) #b의 부모 반환

    if a1<b1:
        parent[b1] = a1
    else:
        parent[a1] = b1
    
result = []

for _ in range(m):
    what, a, b = map(int, sys.stdin.readline().split())

    if what==0:
        union(a, b)

    elif what==1:
        find(a)
        find(b)
        if find(a) == find(b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)