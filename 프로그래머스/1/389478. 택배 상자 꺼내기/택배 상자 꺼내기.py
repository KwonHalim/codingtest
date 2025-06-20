def solution(n, w, num):
    row = 0
    arr = [[0]*w for i in range(int((n / w) + 1))]
    dir = 'right'
    temp = 1
    while(temp<=n):
        if(dir=='right'):
            i = 0
            for i in range (w):
                if(temp == n+1):
                    break
                arr[row][i] = temp
                temp = temp + 1
            row = row + 1
            dir = 'left'
        else:
            for i in range(w):
                if(temp == n+1):
                    break
                arr[row][w-i-1] = temp
                temp = temp + 1
            row = row + 1
            dir = 'right'
            
            
            
    for line in arr:
        print(line)
            
    for i in range(int((n/w) + 1)):
        for j in range (w):
            if(num == arr[i][j]):
                num_row = i
                num_col = j
                
    
    cnt = 0
    a = int(n / w) + 1
    
    while (num_row + 1 < a) and (arr[num_row + 1][num_col] != 0):
        cnt += 1
        num_row += 1
    
    answer = cnt+1
    return answer