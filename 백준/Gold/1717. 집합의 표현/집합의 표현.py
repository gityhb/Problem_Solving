import sys

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]


def union (a, b):
    #각각 대표노드 찾음
    rootA = find(a)
    rootB = find(b)

    #다르면 하나를 다른쪽에 연결
    if rootA != rootB:
        parent[rootB] = rootA

def find(a):
    #자신이 루트노드라면 그 값 반환
    if a == parent[a]:
        return a
    #루트 찾을 때까지 재귀 호출 후 결과 부모 테이블에 갱신
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def checkSame(a, b):
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")
        
for _ in range(m):
    k, a, b = map(int,sys.stdin.readline().split())

    if k==0:
        union(a, b)
    else:
        checkSame(a, b)