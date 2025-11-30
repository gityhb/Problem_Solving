import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

len_a = len(A)
len_b = len(B)

dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len_a][len_b])

result = []
i, j = len_a, len_b

while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        result.append(A[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

if result:
    print("".join(result[::-1]))