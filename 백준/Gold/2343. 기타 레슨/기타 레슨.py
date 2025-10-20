import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

start = max(A)
end = sum(A)

while start<=end:
    middle = (start + end) // 2 #블루레이 크기

    sum = 0 #현 블루레이에 담긴 시간
    count = 0 #사용한 블루레이 개수

    for lecture_time in A:
        if sum + lecture_time > middle:
            count += 1
            sum = 0
        
        sum += lecture_time
    
    if sum != 0:
        count += 1

    if count > M:
        start= middle+1
    
    else: 
        end = middle - 1

print(start)