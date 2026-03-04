def solution(s):
    num = 0
    for i in s:
        if i=='}':
            num+=1    
    
    cnt = 0
    tmp = ""
    li = [[] for i in range(num-1)]
    for i in range(len(s)):
            if '0'<=s[i]<='9':
                tmp += s[i]
            elif s[i] == ',':
                if tmp:
                    li[cnt].append(int(tmp))
                    tmp = ""
            elif s[i] == '}':
                if tmp:
                    li[cnt].append(int(tmp))
                    tmp = ""
                    cnt += 1
            
    li.sort(key = lambda x:len(x))
    
    answer = []
    
    for i in li:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer