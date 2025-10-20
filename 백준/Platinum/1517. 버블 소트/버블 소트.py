import sys

A = []
tmp = []
result = 0  #inversion(Swap) 횟수를 저장할 변수

def merge_sort(s, e):
    global A, tmp, result

    if e-s < 1:
        return
    
    #분할
    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m+1, e)

    #병합
    for i in range(s, e+1):
        tmp[i] = A[i]

    k = s
    index1 = s
    index2 = m+1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]

            result += (index2 - k)

            k += 1
            index2 += 1
        else: 
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(sys.stdin.readline())

A = [0] * (N+1)
tmp = [0] * (N+1)

inputs =list(map(int, sys.stdin.readline().split()))
for i in range(N):
    A[i+1] = inputs[i]

merge_sort(1, N)

print(result)
