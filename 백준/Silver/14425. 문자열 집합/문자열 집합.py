import sys

N, M = map(int, sys.stdin.readline().split())

list = set()
find_list = []

for i in range(N):
    string = sys.stdin.readline()
    list.add(string)

for i in range(M):
    find = sys.stdin.readline()
    find_list.append(find)

count = 0

for check in find_list:
    if check in list:
        count += 1

print(count)