import sys

Min, Max = map(int, sys.stdin.readline().split())

range_size = Max-Min+1
Check = [False] * range_size

i = 2
while i*i <= Max:
    pow_num = i * i

    start_index = Min // pow_num

    if Min % pow_num != 0:
        start_index += 1

    j=start_index
    while pow_num * j <= Max:

        num = pow_num * j
        
        index = num - Min
        Check[index] = True

        j += 1
    
    i += 1

count = 0
for i in range(range_size):
    if not Check[i]:
        count+=1

print(count)
