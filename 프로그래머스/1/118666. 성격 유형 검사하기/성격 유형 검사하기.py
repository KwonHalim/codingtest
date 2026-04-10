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

    type = ""
    if dic["R"] >= dic["T"]:
        type += "R"
    else:
        type += "T"

    if dic["C"] >= dic["F"]:
        type += "C"
    else:
        type += "F"

    if dic["J"] >= dic["M"]:
        type += "J"
    else:
        type += "M"

    if dic["A"] >= dic["N"]:
        type += "A"
    else:
        type += "N"

    return type