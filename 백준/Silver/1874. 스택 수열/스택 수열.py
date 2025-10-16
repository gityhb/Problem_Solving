import sys

N = int(sys.stdin.readline())

stack = []
result = []
count = 1
possible = True # 가능 여부를 저장할 변수

for _ in range(N):
    number = int(sys.stdin.readline())

    while number >= count:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == number:
        stack.pop() #<-- 여기를 수정! 인자 없이 사용
        result.append('-')
    else:
        possible = False # 불가능하다고 표시
        break # 더 이상 진행할 필요 없으므로 반복문 탈출

# 반복문이 모두 끝난 후 마지막에 한 번만 출력
if not possible:
    print('NO')
else:
    for op in result:
        print(op)