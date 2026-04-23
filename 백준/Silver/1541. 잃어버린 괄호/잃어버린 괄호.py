import sys

expr = sys.stdin.readline().strip()
parts = expr.split('-')

first_parts = parts[0].split('+')
result = 0
for num in first_parts:
    result += int(num)

for i in range(1, len(parts)):
    sub_sum = 0
    sub = parts[i].split('+')

    for k in sub:
        sub_sum+= int(k)
    
    result -= sub_sum

print(result)