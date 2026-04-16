def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right
    
    while left <= right:
        mid = (left+right) // 2
        
        total_time = 0
        
        for i in range(len(diffs)):
            if mid >= diffs[i]:
                total_time += times[i]
                
            else:
                k = diffs[i] - mid
                one = times[i]+times[i-1]
                
                total_time += (one*k) + times[i]
            
        if total_time > limit:
            left = mid+1
        elif total_time <= limit:
            right = mid-1
            answer = mid
            
    return answer