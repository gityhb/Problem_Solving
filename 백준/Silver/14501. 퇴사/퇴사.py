#퇴사, 최대이익 구하기
import sys

N = int(sys.stdin.readline())

T = [0] * (N+1) #상담완료기간
P = [0] * (N+1) #상담완료보수
dp = [0] * (N+2)

for i in range(1, N+1):
    T[i], P[i] = map(int, sys.stdin.readline().split())

#뒤에서부터 계산
for i in range(N, 0, -1):
    if i + T[i] > N+1: #상담 시 끝나는 날짜가 퇴사일 넘기는 경우
        dp[i] = dp[i+1]
    
    else: #상담 가능 경우
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
    
print(dp[1])