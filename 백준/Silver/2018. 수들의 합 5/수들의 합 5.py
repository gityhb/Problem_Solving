import sys

N = int(sys.stdin.readline())

count = 1
total_sum = 1
start_index = 1
end_index = 1

while (end_index != N):
    
    if total_sum == N:
        count += 1
        end_index += 1
        total_sum += end_index
        
    elif total_sum > N:
        total_sum -= start_index
        start_index += 1
        
    elif total_sum < N:
        end_index+=1
        total_sum+=end_index

print(count)