import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

plus, minus, gop, na = map(int, sys.stdin.readline().split())

maxN = -1000000000
minN = 1000000000

def back(i, current_num, plus, minus, gop, na):
    global maxN, minN

    if i==N:
        maxN = max(maxN, current_num)
        minN = min(minN, current_num)
        return

    else: 
        if plus>0:
            back(i+1, numbers[i]+current_num, plus-1, minus, gop, na)
        if minus>0:
            back(i+1, current_num-numbers[i], plus, minus-1, gop, na)
        if gop>0:
            back(i+1, numbers[i]*current_num, plus, minus, gop-1, na)
        if na>0:
            back(i+1, int(current_num/numbers[i]), plus, minus, gop, na-1)

a = back(1, numbers[0], plus, minus, gop, na)

print(maxN)
print(minN)