def solution(progresses, speeds):
    answer = []
    idx = 0
    day = 0
    while idx < len(progresses):
        day = 0
        while progresses[idx] < 100:
            for i in range(idx,len(progresses)):
                progresses[i] += speeds[i]
                
                
        while idx < len(progresses) and progresses[idx] >= 100:
            idx +=1
            day+=1
        answer.append(day)
        
    return answer