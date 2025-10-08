import sys

# 최대 1,000,000개의 수를 처리해야 하므로
# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.

def solve():
    """
    N개의 수를 입력받아 오름차순으로 정렬하고 출력합니다.
    """
    # 첫째 줄에서 수의 개수 N을 읽습니다.
    try:
        # 공백 없이 줄바꿈으로 N이 주어지므로, strip()으로 혹시 모를 공백을 제거합니다.
        N = int(sys.stdin.readline().strip())
    except:
        # 입력 오류 시 종료
        return

    # N개의 수를 저장할 리스트
    numbers = []
    
    # N개의 줄에서 각각의 수를 읽어 리스트에 추가합니다.
    for _ in range(N):
        try:
            # sys.stdin.readline()으로 한 줄씩 빠르게 읽습니다.
            number = int(sys.stdin.readline().strip())
            numbers.append(number)
        except:
            # 입력 오류 발생 시, 해당 입력은 건너뜁니다.
            continue
            
    # --- 핵심 로직 ---
    
    # 파이썬의 내장 정렬 함수인 sorted()를 사용합니다.
    # 이는 TimSort 알고리즘 (O(N log N))으로 구현되어 가장 빠르고 효율적입니다.
    numbers.sort()
    
    # --- 출력 ---
    
    # 정렬된 결과를 한 줄에 하나씩 출력합니다.
    # 출력 속도 향상을 위해 print() 대신 sys.stdout.write를 사용할 수도 있습니다.
    # 하지만 print()도 파이썬 3에서는 충분히 빠릅니다.
    for number in numbers:
        print(number)

if __name__ == "__main__":
    solve()