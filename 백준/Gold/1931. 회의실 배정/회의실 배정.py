import sys

N = int(sys.stdin.readline())
meeting=[]

for _ in range(N):
    start, end=map(int, sys.stdin.readline().split())
    meeting.append([end, start])

meeting.sort()

count = 0
end_time=0

for end, start in meeting:
    if start>=end_time:
        count+=1
        end_time=end

print(count)
