def solution(record):
    answer = []
    dic = {}
    
    li = []
        
    for i in record:
        sen = i.split(" ")
        # print(sen)
        if sen[0] == "Change" or sen[0] == "Enter":
            if sen[1] in dic:
                dic[sen[1]] = sen[2]
            else:
                dic[sen[1]] = sen[2]
            
    # print(dic)
    
    for i in record:
        enter, uid = i.split(" ")[0], i.split(" ")[1]
        if enter == "Enter":
            answer.append(dic[uid] + "님이 들어왔습니다.")
        elif enter == "Leave":
            answer.append(dic[uid] + "님이 나갔습니다.")
    return answer