def solution(dartResult):
    answer = 0
    s = ''
    li = []
    for dart in dartResult:
        if dart.isdigit():
            s+=dart
            
        elif dart in ['S','D','T']:
            s = int(s)
            if dart == 'S':
                pass
            elif dart == 'D':
                s*=s
            elif dart== 'T':
                s= s*s*s
            li.append(s)
            s = ''
            
        if dart in ['*','#']:
            if dart == '*':
                if len(li) > 1:
                    li[-1] = li[-1] * 2
                    li[-2] = li[-2] * 2
                else:
                    li[-1] = li[-1] * 2
            else:
                li[-1] *= -1
        # print(li)
            
    return sum(li)