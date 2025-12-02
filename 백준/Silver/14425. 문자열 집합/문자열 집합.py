import sys

N, M = map(int, sys.stdin.readline().split())

trie = {}

#집합 S의 문자열 트라이에 넣기
for _ in range(N):
    word = sys.stdin.readline().strip()
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
    
    current["_end"] = True

count=0
for _ in range(M):
    word = sys.stdin.readline().strip()
    current = trie
    is_exist = True

    #한글자씩 훑음
    for char in word:
        if char not in current:
            is_exist = False
            break
        current = current[char]
    
    if is_exist and "_end" in current:
        count+=1

print(count)