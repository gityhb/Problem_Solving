import sys
 
N = int(sys.stdin.readline())
result = []
stack = []
count = 1
possible = True

for i in range(N):
    num = int(sys.stdin.readline())

    while num >= count:
        stack.append(count)
        result.append('+')
        count+=1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
   
    else:
        possible = False
        break

if not possible:
    print('NO')
else:
    for i in result:
        print(i)