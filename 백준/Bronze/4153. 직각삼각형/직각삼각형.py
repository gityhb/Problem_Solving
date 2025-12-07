import sys

result = []

while(True):
    a, b, c= map(int, sys.stdin.readline().split())

    if a==0 and b==0 and c==0:
        break

    if max(a, b, c) == a:
        if a**2 == b**2+c**2:
            result.append("right")
        else: result.append("wrong")
    
    elif max(a, b, c) == b:
        if b**2 == a**2+c**2:
            result.append("right")
        else: result.append("wrong")
    
    elif max(a, b, c) == c:
        if c**2 == a**2+b**2:
            result.append("right")
        else: result.append("wrong")

for i in result:
    print(i)