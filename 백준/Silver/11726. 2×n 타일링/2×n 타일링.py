import sys

n = int(sys.stdin.readline())

array = [0] * 1001

array[1] = 1
array[2] = 2

for i in range(3, n+1):
    array[i] = (array[i-2]+array[i-1]) % 10007

print(array[n])