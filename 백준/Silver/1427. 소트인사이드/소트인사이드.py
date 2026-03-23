import sys

numbers = list(map(int, sys.stdin.readline().strip()))

new = sorted(numbers, reverse=True)

print(*new, sep='')