import sys

N = int(sys.stdin.readline())

list1 = []

for _ in range(N):
    num = int(sys.stdin.readline())
    
    list1.append(num)

list1.sort()

for k in list1:
    print(k)