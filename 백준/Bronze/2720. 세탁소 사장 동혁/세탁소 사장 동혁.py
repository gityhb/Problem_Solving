import sys

T = int(sys.stdin.readline())
total = []

for _ in range(T):
    money = int(sys.stdin.readline())
    result = [0] * 4

    if money >= 25:
        result[0] = money//25
        money = money - (25*(money//25))

    if money >= 10:
        result[1] = money//10
        money = money - (10*(money//10))

    if money >= 5:
        result[2] = money//5
        money = money - (5*(money//5))

    if money >= 1:
        result[3] = money//1
        money = money - (1*(money//1))

    total.append(result)


for i in total:
    print(*i)