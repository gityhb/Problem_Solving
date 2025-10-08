import math

def sieve(M, N):
    A = [True] * (N + 1)  # 소수 여부 표시 (처음엔 모두 소수라 가정)
    A[0] = A[1] = False   # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(N)) + 1):
        if A[i]:
            for j in range(i * i, N + 1, i):  # 배수 지우기
                A[j] = False

    for i in range(M, N + 1):
        if A[i]:
            print(i)

# 실행 부분
M, N = map(int, input().split())
sieve(M, N)
