import sys

xlist = []
ylist = []
result=[]

for _ in range(3):
    x, y = sys.stdin.readline().split()
    xlist.append(x)
    ylist.append(y)

y4=0
x4= 0

if xlist.count(xlist[0]) == 1:
    x4 = xlist[0]
elif xlist.count(xlist[1]) == 1:
    x4 = xlist[1]
else:
    x4 = xlist[2]

if ylist.count(ylist[0]) == 1:
    y4 = ylist[0]
elif ylist.count(ylist[1]) == 1:
    y4 = ylist[1]
else:
    y4 = ylist[2]

print(x4, y4)