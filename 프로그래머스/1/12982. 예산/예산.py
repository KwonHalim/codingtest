def solution(d, budget):
    answer = 0
    d.sort()
    # print(d)
    idx = 0
    while idx < len(d):
        budget -= d[idx]
        if budget < 0:
            break
        else:
            answer+=1
            idx+=1
    return answer