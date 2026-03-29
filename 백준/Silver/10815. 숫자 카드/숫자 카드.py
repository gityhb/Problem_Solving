import sys

N = int(sys.stdin.readline())

num1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

find = list(map(int, sys.stdin.readline().split()))

result = []
num1.sort()

for i in range(M):
    start = 0
    end = N-1

    while start<=end:
        mid = (start+end)//2
        if find[i] == num1[mid]:
            result.append(1)
            break
        elif find[i] > num1[mid]:
            start = mid+1
        elif find[i] < num1[mid]:
            end = mid-1

    else: result.append(0)

print(*result)