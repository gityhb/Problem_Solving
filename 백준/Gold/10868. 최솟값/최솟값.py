import sys

N, M = map(int, sys.stdin.readline().split())

k = 0
while 2**k<N:
    k+=1
start_index = 2**k
tree = [1000000001] * (2**k * 2)

for i in range(N):
    tree[start_index+i] = int(sys.stdin.readline())

for i in range(start_index-1, 0, -1):
    tree[i] = min(tree[i*2], tree[i*2+1])

def get_min(start, end):
    start = start+start_index-1
    end = end+start_index-1

    min_val = 1000000001
    while start<=end:
        if start%2 ==1:
            if min_val > tree[start]:
                min_val = tree[start]
            start += 1
        if end%2==0:
            if min_val > tree[end]:
                min_val = tree[end]
            end-=1
        
        start//=2
        end//=2
    
    return min_val

result = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    result.append(get_min(a, b))

for i in result:
    print(i)