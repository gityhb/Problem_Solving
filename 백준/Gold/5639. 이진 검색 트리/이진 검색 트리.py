import sys
sys.setrecursionlimit(10**6)
nums = []

while True:
    try:
        num = int(sys.stdin.readline())
        if not num:
            break
        nums.append(num)
    except:
        break

def tree(start, end):
    if start>end: #리스트에 숫자 하나 남았을때
        return
    
    root = nums[start] #루트는 첫 인자
    idx = end+1

    for i in range(start+1, end+1):
        if root < nums[i]:
            idx = i
            break
        
    tree(start+1, idx-1) #start는 현 루트여서 제외
    tree(idx, end)
    print(root)

tree(0, len(nums)-1)