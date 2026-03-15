from collections import deque

def solution(storage, requests):
    answer = 0
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    box = [['' for i in range(len(storage[0])+2)]for j in range(len(storage)+2)]
    
    for i in range(1,len(storage)+1):
        for j in range(1, len(storage[0])+1):
            box[i][j] = storage[i-1][j-1]
            
            
    queue = deque()
    for request in requests:
        if len(request) == 2:
            for row in range(len(box)):
                for col in range(len(box[0])):
                    if box[row][col] == request[0]:
                        box[row][col] = ''
        else:
            visited = [[False for i in range(len(box[0]))] for j in range(len(box))]
            queue.append((0,0))
            
            while queue:
                r,c = queue.popleft()
                visited[r][c] = True
                
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0<=nr<len(box) and 0<=nc<len(box[0]):
                        if box[nr][nc] == '' and not visited[nr][nc]:
                            queue.append((nr,nc))
                            visited[nr][nc] = True
                        elif box[nr][nc] == request:
                            box[nr][nc] = ''
                            visited[nr][nc] = True
    answer = 0
    for row in box:
        for col in row:
            if col != '':
                answer+=1
                

    return answer