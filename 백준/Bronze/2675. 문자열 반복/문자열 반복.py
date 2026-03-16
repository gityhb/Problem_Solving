import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    R, S = sys.stdin.readline().split()

    string = ''

    for char in S:
        for _ in range(int(R)):
            string += char

    result.append(string)

for i in result:
    print(i)