import sys

N = int(sys.stdin.readline())
strings = list(map(str, sys.stdin.readline().strip()))

count = 0
for i in strings:
    if i == "S":
        count+=1
    else: count+=0.5

print(min(N, int(count+1)))
