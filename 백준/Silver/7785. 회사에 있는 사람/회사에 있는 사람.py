import sys

n = int(sys.stdin.readline())

S = set()

for _ in range(n):
    name, status = sys.stdin.readline().split()

    if status == "enter":
        S.add(name)
    else:
        S.remove(name)
    
for i in sorted(S, reverse=True):
    print(i)
