import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    stack = []
    a = sys.stdin.readline().strip()
    vps = True

    for i in a:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                vps = False
                break
            else:
                stack.pop()
    
    if vps and not stack:
        result.append("YES")
    else: result.append("NO")

for i in result:
    print(i)