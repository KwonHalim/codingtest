from itertools import combinations

def solution(n, q, ans):
    answer = 0
    li = []
    for i in range(1,n+1):
        li.append(i)
    
    for i in combinations(li,5):
        set_code = set(i)
        
        for i in range(len(q)):
            match = len(set_code & set(q[i]))
            if match != ans[i]:
                break
                
        else:
            answer+=1
            
    return answer