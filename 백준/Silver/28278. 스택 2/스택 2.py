import sys

N = int(sys.stdin.readline())
result = []
stack = []

for _ in range(N):
    n = sys.stdin.readline().split()
    m = int(n[0])

    if m == 1:
        stack.append(int(n[1]))

    elif m == 2:
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())

    elif m == 3:
        result.append(len(stack))

    elif m == 4:
        if stack:
            result.append(0)
        else:
            result.append(1)
            
    elif m == 5:
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

for i in result:
    print(i)