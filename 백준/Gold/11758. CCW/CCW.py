import sys

dot = []

for _ in range(3):
    x, y=map(int, sys.stdin.readline().split())
    dot.append([x, y])

ccm1 = (dot[1][0]-dot[0][0])*(dot[2][1]-dot[0][1])
ccm2 = (dot[2][0]-dot[0][0])*(dot[1][1]-dot[0][1])

ccm = ccm1-ccm2

if ccm>0:
    print(1)
elif ccm <0:
    print(-1)
else: print(0)