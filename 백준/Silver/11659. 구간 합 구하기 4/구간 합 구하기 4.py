import sys

# 1. 수의 개수 N과 구해야 하는 횟수 M을 입력받기
N, M = map(int, sys.stdin.readline().split())

# 2. N개의 수 입력 받기
numbers = list(map(int, sys.stdin.readline().split()))

# 3. 누적합 배열 만들기. (numbers 배열 합 저장), 첫 요소 0
prefix_sum = [0] * (N+1) 

# 4. 누적합 배열 채우기
for i in range(N):
    prefix_sum[i+1]=prefix_sum[i]+numbers[i]

# 5. M개의 구간 i, j 결과 처리
result = []

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    range_sum = prefix_sum[j]-prefix_sum[i-1]

    result.append(str(range_sum))

sys.stdout.write('\n'.join(result)+'\n')