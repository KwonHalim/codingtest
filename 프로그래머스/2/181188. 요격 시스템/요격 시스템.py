def solution(targets):
    targets.sort(key=lambda x: (x[1],x[0])) 
    
    answer = 1
    point = targets[0][1] - 0.00001
    
    for i in range(1, len(targets)):
        if point < targets[i][0]:
            point = targets[i][1] - 0.0001
            answer+=1
            
    return answer