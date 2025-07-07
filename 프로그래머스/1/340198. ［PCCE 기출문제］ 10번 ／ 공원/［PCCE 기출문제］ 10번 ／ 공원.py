def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    
    dp = [[0] * cols for _ in range(rows)]
    
    max_square_side = 0 
    
    for i in range(rows):
        for j in range(cols):
            if park[i][j] == "-1":
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                if dp[i][j] > max_square_side:
                    max_square_side = dp[i][j]
    print(dp)
    mats.sort(reverse=True)
    answer = -1
    for val in mats:
        if val <= max_square_side:
            answer = val
            break
            
    return answer