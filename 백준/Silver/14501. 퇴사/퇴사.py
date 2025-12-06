import sys

N = int(sys.stdin.readline())

T= [0] * (N+1)
P = [0] * (N+1)

for i in range(1, N+1):
    T[i], P[i] = map(int, sys.stdin.readline().split())

plans = [0] * (N+5)

for i in range(N, 0, -1):
    if i+T[i] > N+1:
        plans[i] = plans[i+1]
    
    else:
        plans[i] = max(plans[i+1], P[i]+plans[i+T[i]])

print(plans[1])