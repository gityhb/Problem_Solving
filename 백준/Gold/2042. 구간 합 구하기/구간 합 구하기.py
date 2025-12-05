import sys

N, M, K = map(int, sys.stdin.readline().split())

#1. 트리배열 초기화
k=0
while 2**k<N:
    k+=1
start_index = 2**k
tree = [0] * (start_index *2)

#리프노드 채움
for i in range(N):
    tree[start_index+i] = int(sys.stdin.readline())

#상위 노드 채움
for i in range(start_index-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2+1]


#업데이트 함수
def update(index, value):
    index = index+start_index-1
    tree[index] = value

    while index > 1:
        index= index//2
        tree[index]=tree[index*2] + tree[index*2+1]

#구간합 합수
def hap(start, end):
    start = start+start_index -1
    end = end+start_index-1

    sum = 0
    
    while start<=end:
        if start % 2 == 1: #부모 노드 옮기기 위해
            sum += tree[start]
            start+=1
        if end % 2 == 0: #부모노드 옮기기 위해
            sum += tree[end]
            end -= 1
            
        start//=2
        end//=2

    return sum

result = []

for _ in range(M+K):
    a, b, c= map(int, sys.stdin.readline().split())
    if a==1:
        update(b, c)
    else:
        result.append(hap(b, c))

for i in result:
    print(i)