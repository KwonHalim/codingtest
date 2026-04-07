def solution(storey):
    answer = 0
    while storey != 0:
        tmp = storey % 10
        if tmp > 5:
            cnt = 10 - tmp
            storey += cnt
            answer += cnt
        elif tmp < 5:
            storey -= tmp
            answer += tmp
        else:
            next_digit = (storey // 10) % 10
            if next_digit >= 5:
                storey += 5
                answer += 5
            else:
                storey -= 5  
                answer += 5
        storey //= 10
    return answer