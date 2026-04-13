from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    # print(dic)
    
    
    ls = []
    
    for i in range(10):
        ls.append(discount[i])
        
    first = Counter(ls)
    
    for j in dic:
        if dic[j] > first[j]: 
            break
    else:
        answer += 1
    
    # print(Counter(ls))
    
    for i in range(10,len(discount)):
        # print(i)
        ls.pop(0)
        ls.append(discount[i])
        # print(Counter(ls))
        count_discount = Counter(ls)
        
        for j in dic:
            # print(j)
            if dic[j] > count_discount[j]:
                break
        else:
            answer+=1
            
            
        
    return answer