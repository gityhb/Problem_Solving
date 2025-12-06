import sys

N = int(sys.stdin.readline())

array = [0] * 91
array[1] = 1
array[2] = 2

for i in range(2, 91):
    array[i] = array[i-1]+array[i-2]

print(array[N])