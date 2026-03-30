import sys

n = int(sys.stdin.readline())
en = set()

for _ in range(n):
    name, el = map(str, sys.stdin.readline().split())
    if el == "enter":
        en.add(name)
    elif el == "leave":
        if name in en:
            en.remove(name)

s = sorted(en, reverse=True)

for i in s:
    print(i)