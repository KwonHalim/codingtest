def solution(progresses, speeds):
    answer = []
    idx = 0
    day = 0
    while idx < len(progresses)-1:
        day = 0
        while progresses[idx] < 100:
            for i in range(idx,len(progresses)):
                progresses[i] += speeds[i]
        while progresses[idx] >= 100:
            if idx >= len(progresses)-1:
                if progresses[idx] >= 100:
                    day+=1
                    break
            idx+=1
            day+=1
        answer.append(day)
        print(progresses, answer, idx)
    day = 1
    
    if progresses[-1] < 100:
        while progresses[-1] >= 100:
            day+=1
            progresses[-1] += speeds[-1]
        answer.append(day)
    
    return answer