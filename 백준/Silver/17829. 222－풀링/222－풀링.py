import sys

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def pool(x, y, n):
    if n == 2:
        elements = [
            matrix[x][y],
            matrix[x][y+1],
            matrix[x+1][y],
            matrix[x+1][y+1]
        ]
        elements.sort()
        return elements[2]

    half = n//2
    
    top_left = pool(x, y, half)
    top_right = pool(x, y + half, half)
    bottom_left = pool(x + half, y, half)
    bottom_right = pool(x + half, y + half, half)
    
    results = [top_left, top_right, bottom_left, bottom_right]
    results.sort()
    return results[2]

answer = pool(0, 0, N)
print(answer)