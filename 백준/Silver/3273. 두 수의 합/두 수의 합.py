import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

numbers.sort()

start = 0
end = n - 1
count = 0

while start < end:
    s = numbers[start] + numbers[end]

    if s == x:
        count += 1
        start += 1
        end -= 1
    elif s < x:
        start += 1
    else:
        end -= 1

print(count)