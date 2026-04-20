import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

winner = 'D'
a_num = 0
b_num = 0

for i in range(len(A)):
    if A[i] > B[i]:
        winner = 'A'
        a_num+=3
    elif A[i] < B[i]:
        winner = 'B'
        b_num+=3
    else:
        a_num+=1
        b_num+=1

print(a_num, b_num)

if a_num == b_num:
    print(winner)
elif a_num > b_num:
    print('A')
else: print('B')