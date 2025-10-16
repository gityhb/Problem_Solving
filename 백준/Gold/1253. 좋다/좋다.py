import sys

N = int(sys.stdin.readline())

numbers=list(map(int, sys.stdin.readline().split()))

numbers.sort() #정렬 완료

count = 0

for i in range(0, N):
    k = numbers[i]
    start_index = 0
    end_index = N-1
    
    while(start_index < end_index):
        total_sum = numbers[start_index] + numbers[end_index]
        
        if(total_sum == k): #자기 자신x
            if start_index == i: start_index += 1
            elif end_index == i: end_index -= 1
            else:
                count += 1
                break
        
        elif(total_sum > k):
            end_index -= 1

        elif(total_sum < k):
            start_index += 1
    
print(count)