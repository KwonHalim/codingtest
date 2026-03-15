def solution(clothes):
    dic = {}
    cnt = 0
    for cloth, kind in clothes:
        if kind in dic:
            dic[kind] +=1
        else:
            dic[kind] = 2
    
    answer = 1
    for i in dic:
        answer *= dic[i]
    
        
    
    

    return answer -1 