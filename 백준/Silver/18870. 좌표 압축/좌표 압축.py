import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr_set = set(arr)
arr_sort = sorted(arr_set)

rank_dict = {}

for i in range(len(arr_sort)):
    num = arr_sort[i]
    rank_dict[num] = i

for num in arr:
    print(rank_dict[num], end=' ')