import sys

# 1. 표의 크기 N과 횟수 M 입력 받기
N, M= map(int, sys.stdin.readline().split())

# 2. 누적합 배열 초기화
D = [[0]*(N+1) for _ in range(N+1)]

# 3. 원본 배열 A 입력 및 누적 합 배열 D 채우기
result = []
for i in range(1, N+1):
    row_data = list(map(int, sys.stdin.readline().split()))

    for j in range(1, N+1):
        #원본 값
        A_ij = row_data[j-1]

        #누적 합 배열
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A_ij
    
# 4. M개의 구간 합
outputs = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]

    outputs.append(str(result))

# 5. 결과 출력
sys.stdout.write('\n'.join(outputs)+'\n')
