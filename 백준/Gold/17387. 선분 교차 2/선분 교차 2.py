import sys

AB = list(map(int, sys.stdin.readline().split()))
CD = list(map(int, sys.stdin.readline().split()))

A = [AB[0], AB[1]]
B = [AB[2], AB[3]]
C = [CD[0], CD[1]]
D = [CD[2], CD[3]]

def ccm(A, B, C):
    result = ((A[0]*B[1])+(B[0]*C[1])+(C[0]*A[1]))-((A[1]*B[0])+(B[1]*C[0])+(C[1]*A[0]))
    return result

abc = ccm(A, B, C)
abd = ccm(A, B, D)
cda = ccm(C, D, A)
cdb = ccm(C, D, B)

if abc*abd ==0 and cda*cdb==0:
    if A>B: A, B = B, A
    if D<C: C, D = D, C
    
    if A<=D and C<=B:
        print(1)
    else:
        print(0)

elif abc*abd <=0 and cda*cdb<=0:
    print(1)


else:
    print(0)