import sys

S, P = map(int, sys.stdin.readline().split())

strings = sys.stdin.readline().strip() 

min_counts = list(map(int, sys.stdin.readline().split()))

min_cond = 0
current_counts = [0] * 4
count = 0 

for i in range(4):
    if min_counts[i] == 0:
        min_cond += 1

char_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(P):
    char = strings[i]
    idx = char_map[char]
    current_counts[idx] += 1
    if current_counts[idx] == min_counts[idx]:
        min_cond += 1

if min_cond == 4:
    count += 1

for i in range(P, S):
    new_char = strings[i]
    new_idx = char_map[new_char]
    current_counts[new_idx] += 1
    if current_counts[new_idx] == min_counts[new_idx]:
        min_cond += 1
    
    old_char = strings[i - P]
    old_idx = char_map[old_char]
    if current_counts[old_idx] == min_counts[old_idx]:
        min_cond -= 1
    current_counts[old_idx] -= 1

    if min_cond == 4:
        count += 1

print(count)