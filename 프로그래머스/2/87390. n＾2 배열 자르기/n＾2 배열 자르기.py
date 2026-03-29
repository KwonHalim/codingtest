def solution(n, left, right):
    answer = []
# 1 2 3
# 2 2 3
# 3 3 3


# 3,2,2,3 -> 2

# 00 01 02
# 10 11 12
# 20 21 22

    
    for i in range(left,right+1):
        row = i // n
        col = i % n
        answer.append(max(row,col) + 1)
            
    return answer