import sys

N, M = map(int, sys.stdin.readline().split())

A = set() #못들어본 사람 집합
B = set() #못본사람 집합

for _ in range(N):
    people = sys.stdin.readline().strip()
    A.add(people)

for _ in range(M):
    people = sys.stdin.readline().strip()
    B.add(people)

C = A & B

print(len(C))
for char in sorted(C):
    print(char)