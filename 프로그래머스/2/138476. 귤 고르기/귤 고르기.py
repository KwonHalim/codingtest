def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
           
    li = []
    for i in dic.values():
        li.append(i)
    # print(dic)
    li.sort(reverse=True)
    # print(li)
    sum = 0
    cnt=0
    while sum < k:
        sum+=li[cnt]
        cnt+=1
    
    return cnt