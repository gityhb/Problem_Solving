import sys

N = int(sys.stdin.readline())
count = 0
arr = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    arr.append([int(age), count, name])
    count += 1

arr.sort()

for a, b, c in arr:
    print(a, c)