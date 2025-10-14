import sys

# 1. 총 과목 갯수 입력
try: 
    N=int(sys.stdin.readline())
except:
    N=0

# 2. 과목별 점수 입력
scores=list(map(int, sys.stdin.readline().split()))

# 3. 최고점
Max = max(scores)

# 4. 새로운 평균
new_avg = sum(scores)/N/Max * 100

print(new_avg)