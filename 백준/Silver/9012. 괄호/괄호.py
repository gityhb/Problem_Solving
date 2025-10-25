import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    PS = sys.stdin.readline().strip()
    stack= []
    vps = True

    for char in PS:
        if char == '(':
            stack.append('char')
        
        elif char == ')':
            if not stack:
                vps = False
                break
            else: stack.pop()
        
    if stack:
        vps = False
    
    if vps:
        result.append("YES")
    else:
        result.append("NO")

for res in result:
    print(res)