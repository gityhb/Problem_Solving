import sys

N = int(sys.stdin.readline())

strings = str(sys.stdin.readline()).strip()
sum = 0

for char in strings:
    sum += int(char)

print(sum)