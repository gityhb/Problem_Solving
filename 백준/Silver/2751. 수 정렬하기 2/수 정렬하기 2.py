import sys

# 1. 수의 개수 N을 입력받습니다.
# 입력 속도 향상을 위해 sys.stdin.readline()을 사용합니다.
# 입력 끝에 붙는 공백/줄바꿈 문자를 제거하지 않고 바로 int()로 변환합니다.
try:
    # N을 입력받지 못하면 0으로 처리합니다.
    N = int(sys.stdin.readline())
except:
    N = 0

# 2. N개의 수를 읽어 리스트에 저장합니다.
numbers = []
for _ in range(N):
    try:
        # 한 줄씩 수를 읽어 리스트에 추가합니다.
        numbers.append(int(sys.stdin.readline()))
    except:
        # 입력 오류 발생 시 건너뜁니다.
        continue

# 3. 리스트를 오름차순으로 정렬합니다.
# 파이썬의 내장 .sort() 함수는 매우 빠릅니다.
numbers.sort()

# 4. 정렬된 결과를 한 번에 출력합니다.
# 정렬된 숫자들을 문자열로 변환하고 줄바꿈 문자('\n')로 모두 연결합니다.
# 이렇게 한 번에 출력하는 것이 반복문에서 print()를 여러 번 호출하는 것보다 빠릅니다.
output = '\n'.join(map(str, numbers))

# sys.stdout.write()를 사용하여 결과를 출력합니다.
# 마지막에 줄바꿈 문자를 한 번 더 추가하여 출력을 마무리합니다.
sys.stdout.write(output + '\n')