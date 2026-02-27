from collections import deque
def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] =='R'):
                x=i
                y=j
            if(board[i][j] =='G'):
                gx=i
                gy=j
    
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    
    visited = [[False] * len(board[0]) for i in range(len(board))]
    
    visited[x][y] = True
    
    queue = deque()
    
    pos = (x,y,0)
    
    queue.append(pos)
    
    while (queue):
        curr = queue.popleft()
        if((curr[0] == gx) and (curr[1] == gy)):
            return curr[2]
        
        for i in range(4):
            nx, ny = curr[0], curr[1]
            while 0 <= nx + dx[i] < len(board) and 0 <= ny + dy[i] < len(board[0]) and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, curr[2] + 1))
    return -1