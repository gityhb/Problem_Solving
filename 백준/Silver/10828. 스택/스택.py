import sys

stack = []

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    
    one = command[0] 

    if one == "push":
        stack.append(command[1])
        
    elif one == "pop":
        if not stack:
            print("-1")
        else:
            print(stack.pop())
            
    elif one == "size":
        print(len(stack))
        
    elif one == "empty":
        print(1 if not stack else 0)
        
    elif one == "top":
        if not stack:
            print("-1")
        else:
            print(stack[-1])