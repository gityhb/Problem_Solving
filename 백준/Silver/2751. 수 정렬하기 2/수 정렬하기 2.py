import sys

try:
    N = int(sys.stdin.readline())
except:
    N = 0

numbers = []
for _ in range(N):
    try:
        numbers.append(int(sys.stdin.readline()))
    except:
        continue

numbers.sort()

output = '\n'.join(map(str, numbers))

sys.stdout.write(output + '\n')

