def solution(id_list, report, k):
    answer = []
    dic = {}
    li = []
    sen = list(set(report))
    for peo in sen:
        a,b = peo.split(" ")
        # print(a,b)
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
    # print(dic)
    for names in dic.items():
        name, num = names
        # print(name,num)
        if num >= k:
            li.append(name)
            
    # print(li)
    # print(sen)
    
    mail_count = {}
    
    for people in sen:
        a,b = people.split(" ")
        if b in li:
            if a not in mail_count:
                mail_count[a] = 1
            else:
                mail_count[a] +=1
    # print(mail_count)
    
    for id in id_list:
        if id in mail_count.keys():
            answer.append(mail_count[id])
        else:
            answer.append(0)
    return answer