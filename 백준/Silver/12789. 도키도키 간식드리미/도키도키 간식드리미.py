import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

stack=[]
target=1

for i in num:
    stack.append(i)
    
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if not stack:
    print("Nice")
else:
    print("Sad")