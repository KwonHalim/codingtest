def check_op(now, op_start, op_end):
    if(op_start<=now<=op_end):
        return op_end
    else:
        return now
    
    
def to_time(time):
    min = int(time[:2])
    sec = int(time[3:5])
    now = min * 60 + sec
    return now


def check_len(now, video_len):
    if now > video_len:
        return video_len
    else:
        return now
    


def solution(video_len, pos, op_start, op_end, commands):    
    now = to_time(pos)
    start = to_time(op_start)
    end = to_time(op_end)
    len = to_time(video_len)
    for command in commands:        
        now = check_op(now, start, end)
        if(command=='next'):
            now = now + 10
        elif(command=='prev'):
            now = now - 10
            if(now < 0):
                now = 0
        print(f"현재 시간 {now}")
        now = check_len(now, len)
        now = check_op(now, start, end)
    min = now // 60
    print(f"min : {min}")
    sec = now % 60
    print(f"sec : {sec}")
    
    answer = f"{min:02d}:{sec:02d}" 
    return answer