import sys

N = int(sys.stdin.readline()) #숫자 개수

card_list = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

card_check = list(map(int, sys.stdin.readline().split()))

result = []

for check in card_check:
    if check in card_list:
        result.append(1)
    else:
        result.append(0)

print(*result)