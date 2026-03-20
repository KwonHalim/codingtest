def solution(picks, minerals):
#     캘 수 있는 개수
    mine = sum(picks)
    dic = {}
    ran = []
    flag = False
    answer = 0
    for i in range(mine):
        dic = {}
        diamond = 0
        iron = 0
        stone = 0
        for j in range(5):
            if 5*i+j >= len(minerals):
                print(5*i+j)
                flag = True
                break
            elif minerals[5*i+j] == "diamond":
                diamond+=1
            elif minerals[5*i+j] == "iron":
                iron+=1
            elif minerals[5*i+j] == "stone":
                stone+=1
        dic["diamond"] = diamond
        dic["iron"] = iron
        dic["stone"] = stone
        ran.append(dic)
        if flag:
            break
        
    ran.sort(key=lambda x: (-x["diamond"], -x["iron"], -x["stone"]))
    # print(ran)
    
    
    for i in range(len(ran)):
        if picks[0] > 0:
            answer += ran[i]["diamond"] + ran[i]["iron"] + ran[i]["stone"]
            picks[0] -= 1
        elif picks [1] > 0:
            answer += ran[i]["diamond"]*5 + ran[i]["iron"] + ran[i]["stone"]
            picks[1] -= 1
        else:
            answer += ran[i]["diamond"]*25 + ran[i]["iron"]*5 + ran[i]["stone"]
        
            
    return answer