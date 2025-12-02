import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    phone_book = [sys.stdin.readline().strip() for _ in range(n)]

    phone_book.sort()

    trie = {}
    consistent = True

    for phone in phone_book:
        current = trie
        for char in phone:
            #딕셔너리 안에 딕셔너리 넣기
            if char not in current:
                current[char] = {}
            current = current[char]

            if "_end" in current:
                consistent = False
                break
        
        current["_end"] = True

        if not consistent:
            break
    
    if consistent:
        print("YES")
    else:
        print("NO")