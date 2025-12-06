import sys

N = int(sys.stdin.readline())

array= [0] * (N+1)

for i in range(2, N+1):
    array[i] = array[i-1]+1

    if i % 2 ==0:
        array[i] = min(array[i], array[i//2]+1)
    
    if i % 3 ==0:
        array[i] = min(array[i], array[i//3]+1)
    
print(array[N])