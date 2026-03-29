def solution(operations):
    answer = []
    
    for a in operations:
        operation, num = a.split(" ")
        if operation == "I":
            answer.append(int(num))
        elif operation == "D":
            if num == '-1':
                if len(answer)!=0:
                    answer.pop()
            else:
                if len(answer)!=0:
                    answer.pop(0)
                else:
                    pass
        answer.sort(reverse=True)
        # print(answer)
                
    
    if len(answer) == 0:
        return [0,0]
    else:
        return [answer[0],answer[-1]]