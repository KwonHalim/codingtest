from itertools import combinations
def solution(orders, course):
    answer = []
    
    dic = {}
            
            
    for k in course:
        for i in orders:
            for j in combinations(sorted(i),k):
                if j not in dic:
                    dic[j] = 1
                else:
                    dic[j]+=1
            
            
    s_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    # print(s_dic)
    
    li = []
    
    for k in course:
        m = 0
        for com, cnt in s_dic:
            if len(com) == k:
                if cnt==1:
                    continue
                elif m <= cnt:
                    m = cnt
                    li.append(com)
                else:
                    break
                    
    li.sort()
    for i in li:
        word=''
        for j in i:
            word +=j
        answer.append(word)
            
            
    return answer