def solution(s):
    answer = True
    
    li = []
    for i in s:
        if i == '(':
            li.append('(')
        else:
            if len(li) == 0:
                return False
            li.pop()
    if li:
        return False
    else:
        return True