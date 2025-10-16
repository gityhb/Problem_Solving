import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

count = 0
start_index = 0
end_index = N-1

while(start_index < end_index):
    sum = numbers[start_index] + numbers[end_index]
    if sum == M:
        count += 1
        start_index += 1

    elif sum > M:
        end_index -= 1
    
    elif sum < M:
        start_index += 1

print(count)
