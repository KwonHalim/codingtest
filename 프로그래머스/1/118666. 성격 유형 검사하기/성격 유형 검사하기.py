def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    idx = 0
    
    for i in choices:
        # print(survey[0])
        if i<4:
            # survey[idx][0]+=i
            # print(survey[idx][0])
            dic[survey[idx][0]] += 4-i
        elif i>4:
            # survey[idx][1]+=i
            # print(survey[idx][1])
            dic[survey[idx][1]] +=i-4
        else:
            pass
        idx+=1
        
        
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for p1, p2 in pairs:
        if dic[p1] >= dic[p2]:
            answer += p1
        else:
            answer += p2
    return answer