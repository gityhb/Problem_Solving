import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))

card_counts = {}
for num in numbers:
    if num in card_counts:
        card_counts[num] += 1
    else:
        card_counts[num] = 1

result = []
for target in find_list:
    count = card_counts.get(target, 0)
    result.append(count)

print(' '.join(map(str, result)))