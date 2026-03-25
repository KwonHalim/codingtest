def solution(s):
    answer = []
    cnt = 0
    t = 0
    while s != '1':
        cnt+= s.count('0')
        s = s.replace('0','')
        s = str(bin(len(s))[2:])
        t+=1

    answer.append(t)
    answer.append(cnt)
        
    return answer