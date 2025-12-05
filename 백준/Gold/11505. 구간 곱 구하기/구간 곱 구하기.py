import sys

N, M, K = map(int, sys.stdin.readline().split())

w = 0
while 2**w < N:
    w+=1
start_index = 2**w
tree=[1] * (start_index * 2)

for i in range(N):
    tree[start_index+i] = int(sys.stdin.readline())

for i in range(start_index-1, 0, -1):
    tree[i] = (tree[i*2] * tree[i*2+1])%1000000007

def update(index, value):
    index = index+start_index-1

    tree[index] = value

    while index>1:
        index=index//2
        tree[index] = (tree[index*2] * tree[index*2+1])%1000000007
    

def gop(start, end):
    start = start+start_index-1
    end = end+start_index-1

    result = 1
    while start<=end:
        if start%2 == 1:
            result = (result*tree[start])%1000000007
            start+=1
        if end%2==0:
            result=(result*tree[end])%1000000007
            end-=1
        
        start//=2
        end//=2
    
    return result

dap = []
for _ in range(M+K):
    a, b, c=map(int, sys.stdin.readline().split())
    if a==1:
        update(b, c)
    else:
        dap.append(gop(b, c))

for i in dap:
    print(i)