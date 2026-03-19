import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    a = int(sys.stdin.readline())

    if a == 0:
        stack.pop()
    else:
        stack.append(a)

hap = 0

for i in stack:
    hap += int(i)

print(hap)