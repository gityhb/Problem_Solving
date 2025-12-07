import sys

N = int(sys.stdin.readline())

xlist= []
ylist=[]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xlist.append(x)
    ylist.append(y)

xlist.append(xlist[0])
ylist.append(ylist[0])

sum1=0
sum2=0

for i in range(N):
    sum1+=xlist[i]*ylist[i+1]
    sum2+=ylist[i]*xlist[i+1]

dap = 1/2*(abs(sum1-sum2))
print("%.1f" % dap)