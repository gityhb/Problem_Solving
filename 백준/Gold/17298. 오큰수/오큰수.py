import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

stack=[]
result=[-1] * N  #정답 배열 모두 -1로 초기화

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        prev_index = stack.pop()
        result[prev_index] = A[i]

    stack.append(i)

print(*result)
