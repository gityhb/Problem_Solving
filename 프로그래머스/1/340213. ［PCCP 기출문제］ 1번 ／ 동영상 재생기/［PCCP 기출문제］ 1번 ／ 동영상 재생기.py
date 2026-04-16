def solution(video_len, pos, op_start, op_end, commands):
    vdo_len = int(video_len[0:2]) * 60 + int(video_len[3:5])
    now = int(pos[0:2]) * 60 + int(pos[3:5])
    op_start = int(op_start[0:2]) * 60 + int(op_start[3:5])
    op_end = int(op_end[0:2]) * 60 + int(op_end[3:5])
    
    if now >= op_start and now <= op_end:
        now = op_end
    
    for i in commands:
        if i == "prev":
            now -= 10
            if now < 0:
                now = 0
        
        else:
            now += 10
            if now > vdo_len:
                now = vdo_len
        
        if now >= op_start and now <= op_end:
            now = op_end
    
    m = now // 60
    s = now % 60
    
    answer = f"{m:02d}:{s:02d}"
        
    return answer