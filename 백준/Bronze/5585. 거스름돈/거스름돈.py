import sys

T = int(sys.stdin.readline())
money = 1000-T

coins = [500, 100, 50, 10, 5, 1]
total = 0

for coin in coins:
    total += money//coin
    money = money % coin

print(total)