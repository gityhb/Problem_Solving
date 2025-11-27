import sys

n = int(sys.stdin.readline())

arr = [1]*46

arr[0] = 0
arr[1] = 1

for i in range(2, 46):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])