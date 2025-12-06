import sys

T = int(sys.stdin.readline())

array = [0] * 11
array[1] = 1
array[2] = 2
array[3]=4

for i in range(4, 11):
    array[i] = array[i-1]+array[i-2]+array[i-3]

result = []

for _ in range(T):
    n = int(sys.stdin.readline())
    result.append(array[n])

for i in result:
    print(i)