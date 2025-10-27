import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

result = []

numbers.sort()

for i in range(M):
    start=0
    end = N-1

    while start<=end:
        mid = (start+end)//2
        if find[i] == numbers[mid]:
            result.append(1)
            break
        elif find[i] > numbers[mid]:
            start = mid+1
        elif find[i] < numbers[mid]:
            end= mid-1

    else:
        result.append(0)

print(' '.join(map(str, result)))