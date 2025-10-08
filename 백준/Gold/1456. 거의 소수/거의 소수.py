import math

def almost_primes(Min, Max):
    limit = 10_000_000
    # 소수 판별 배열
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    count = 0
    # 소수마다 거듭제곱 검사
    for i in range(2, limit + 1):
        if is_prime[i]:
            temp = i
            while temp <= Max / i:
                temp *= i
                if Min <= temp <= Max:
                    count += 1
    return count


# 실행 부분
Min, Max = map(int, input().split())
print(almost_primes(Min, Max))
