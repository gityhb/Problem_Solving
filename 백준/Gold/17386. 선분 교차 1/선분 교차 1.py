import sys

ab = list(map(int, sys.stdin.readline().split()))
cd = list(map(int, sys.stdin.readline().split()))

def ccm(x1, y1, x2, y2, x3, y3):
    ccm_result = ((x1*y2)+(x2*y3)+(x3*y1)) - ((x2*y1)+(x3*y2)+(x1*y3)) 
    return ccm_result

a= ccm(ab[0], ab[1], ab[2], ab[3], cd[0], cd[1]) * ccm(ab[0], ab[1], ab[2], ab[3], cd[2], cd[3])
b= ccm(cd[0], cd[1], cd[2], cd[3], ab[0], ab[1]) * ccm(cd[0], cd[1], cd[2], cd[3], ab[2], ab[3])

if a<0 and b<0:
    print(1)
else: print(0)