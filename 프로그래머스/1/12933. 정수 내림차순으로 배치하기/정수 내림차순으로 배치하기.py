def solution(n):
    answer = ""
    li = []
    while n > 0:
        tmp = n % 10
        li.append(str(tmp))
        n = n // 10
    li.sort(reverse = True)
    
    for i in li:
        answer+=i
    return int(answer)