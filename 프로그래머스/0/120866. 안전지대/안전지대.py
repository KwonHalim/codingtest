def solution(board):
    answer = 0    
    dr = [-1,1,0,0,-1,-1,1,1]
    dc = [0,0,-1,1,-1,1,-1,1]
    
    bomb = [[0 for i in range(len(board[0]))] for i in range(len(board))]
    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                bomb[i][j] = 1
                for k in range(8):
                    if 0 <= i + dr[k] < len(board) and 0 <= j + dc[k] < len(board[0]):
                        bomb[i+dr[k]][j+dc[k]] = 1
    
    for i in bomb:
        for j in i:
            if j == 0:
                answer+=1

    for i in bomb:
        print(i)

    return answer