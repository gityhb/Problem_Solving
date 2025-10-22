import sys
import math

def is_palindrome(target):
    s_str = str(target) #숫자를 문자열로 변환함
    
    s = 0 #문자열의 처음
    e = len(s_str)-1  #문자열의 끝

    while s<e:
        if s_str[s] != s_str[e]:
            return False
        s += 1
        e -= 1
    
    return True

N = int(sys.stdin.readline())
MAX = 1003001

isPrime = [True] * (MAX+1) 

isPrime[0] = isPrime[1] = False

for i in range(2, int(math.sqrt(MAX)+1)):
    if isPrime[i]:
        for j in range(i*2, MAX+1, i):
            isPrime[j] = False

i = N
while True:
    if i > MAX:
        break
    
    if isPrime[i]:
        if is_palindrome(i):
            print(i)
            break
            
    i += 1