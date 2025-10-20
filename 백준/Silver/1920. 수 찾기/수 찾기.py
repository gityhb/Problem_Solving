import sys

#숫자 리스트
N = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
my_cards.sort()

#찾으려는 숫자
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start<=end:
        mid = (start + end) // 2 #중간 인덱스

        if array[mid] == target:
            return 1 #찾았으면 1
        elif array[mid] < target:
            start = mid+1
        elif array[mid] > target:
            end = mid - 1
    
    return 0

for target in targets:
    result = binary_search(my_cards, target)
    print(result)