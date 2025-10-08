#알람시계

import sys

A, B=map(int, sys.stdin.readline().split())

B-=45

if B<0:
    A-=1
    B+=60

    if A<0:
        A=23

print(A, B)
