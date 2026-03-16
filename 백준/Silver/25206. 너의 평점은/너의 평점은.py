import sys

total = 0.0
num_total=0.0

for _ in range(20):
    name, num, jum = sys.stdin.readline().split()

    if jum == 'A+':
        total += float(num) * 4.5
        num_total += float(num)
    elif jum == 'A0':
        total += float(num) * 4.0
        num_total += float(num)
    elif jum == 'B+':
        total += float(num) * 3.5
        num_total += float(num)
    elif jum == 'B0':
        total += float(num) * 3.0
        num_total += float(num)
    elif jum == 'C+':
        total += float(num) * 2.5
        num_total += float(num)
    elif jum == 'C0':
        total += float(num) * 2.0
        num_total += float(num)
    elif jum == 'D+':
        total += float(num) * 1.5
        num_total += float(num)
    elif jum == 'D0':
        total += float(num) * 1.0
        num_total += float(num)
    elif jum == 'F':
        total += float(num) * 0
        num_total += float(num)
    else:
        continue

print(total/num_total)