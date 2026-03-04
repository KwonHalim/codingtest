def solution(name, yearning, photo):
    answer = []

    for n1 in photo:
        sum=0

        for n2 in n1:
            if n2 in name:
                sum+=yearning[name.index(n2)]
        answer.append(sum)
        
    return answer