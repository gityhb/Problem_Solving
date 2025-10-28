import sys
import math

numbers = []
result = []

MAX = 123456
LIMIT = 2 * MAX

is_Prime = [True] * (LIMIT+1)
is_Prime[0] = is_Prime[1] = False

for i in range(2, int(math.sqrt(LIMIT)+1)):
    if is_Prime[i] == True:
        for j in range(i*2, LIMIT+1, i):
            is_Prime[j] = False

while(1):
    N = int(sys.stdin.readline())
    
    count = 0
    
    for i in range(N+1, (2*N)+1):
        if is_Prime[i]:
            count += 1

    result.append(count)

    if N == 0:
        break

for i in range(len(result)):
    if result[i]:
        print(result[i])