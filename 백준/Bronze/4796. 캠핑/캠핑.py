import sys

case_num = 1

while(1):
    L, P, V= map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    
    day = ((V//P * L) + min(V%P, L))

    print(f"Case {case_num}: {day}")

    case_num += 1
