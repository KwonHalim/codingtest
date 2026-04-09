def solution(today, terms, privacies):
    answer = []
    dic = {}
    idx = 1
    
    today_y, today_m, today_d = map(int, today.split('.'))
    today_date = today_y*12*28 + today_m*28 + today_d
    
    for term in terms:
        t, m = term.split(" ")
        # print(t,m)
        dic[t] = m
    # print(dic)
    for privacy in privacies:
            y,m,d = privacy[:4], privacy[5:7], privacy[8:10]
            y = int(y)
            m = int(m)
            d = int(d)
            for i in dic.keys():
                if i == privacy[-1]:
                    m += int(dic[i])
            # print(y,m,d)
            date = y*12*28 + m*28 + d
            
            if today_date >= date:
                answer.append(idx)
            idx+=1
                
    return answer