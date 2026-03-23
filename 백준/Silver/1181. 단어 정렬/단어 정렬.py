import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    abc = sys.stdin.readline().strip()
    
    if [len(abc), abc] in arr:
        continue
    else:
        arr.append([len(abc), abc])

arr.sort()

for i in range(len(arr)):
    print(arr[i][1])