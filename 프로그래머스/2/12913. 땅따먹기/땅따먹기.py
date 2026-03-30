def solution(land):
    answer = 0
    
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            if j == 0:
                land[i][j] += max(land[i-1][1],land[i-1][2],land[i-1][3])         
            elif j == 1:
                land[i][j] += max(land[i-1][0],land[i-1][2],land[i-1][3])
            elif j == 2:
                land[i][j] += max(land[i-1][0],land[i-1][1],land[i-1][3])
            elif j == 3:
                land[i][j] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    return max(land[-1])