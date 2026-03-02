def solution(diffs, times, limit):
    low = 1
    high = 1000000
    answer = high
    
    while low <= high:
        lv = (low + high) // 2
        total_time = 0
        
        for i in range(len(diffs)):
            if i == 0:
                total_time = times[i]
            elif lv >= diffs[i]:
                total_time += times[i]
            else:
                total_time += (diffs[i] - lv) * (times[i] + times[i-1]) + times[i]
        
        if total_time <= limit:
            answer = lv     
            high = lv - 1
        else:
            low = lv + 1
            
    return answer