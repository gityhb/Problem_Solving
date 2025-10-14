import sys

#1. 총 갯수
try:
    N=int(sys.stdin.readline())
except:
    N=0

#2. 한줄의 문자열로 입력
try:
    number=sys.stdin.readline().strip()
except:
    number=""

sum = 0

for num in number:
    sum += int(num)

print(sum)