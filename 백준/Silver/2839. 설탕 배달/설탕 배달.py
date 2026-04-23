import sys

N = int(sys.stdin.readline())
count = 0
while(N>=0):
    if N % 5 == 0:
        count += (N//5)
        print(count)
        break

    N -= 3 #ex) 11이면 -> 8 -> 5 -> 위에 if문에서 걸려서 N=0됨)
    count += 1

if N<0:
    print(-1)