from collections import deque

def solution(maps):
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    visited1 = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    visited2 = [[False for i in range(len(maps[0]))] for j in range(len(maps))]

    l_r = 0
    l_c = 0
    r = 0
    c = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                l_r = i
                l_c = j
            if maps[i][j] == 'S':
                r = i
                c = j
            if maps[i][j] == 'E':
                e_r = i
                e_c = j
                
    # print(l_r, l_c)
    # print(r,c)

    
    queue = deque()
    
    queue.append((r,c,0))
    
    while queue:
        r,c,cnt = queue.popleft()
        visited1[r][c] = True
        
        if r == l_r and c==l_c:
            r = l_r
            c = l_c
            break
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) and visited1[nr][nc] == False and maps[nr][nc] != 'X':
                queue.append((nr,nc,cnt+1))
                visited1[nr][nc] = True
    
    
    if(visited1[l_r][l_c]) == False:
        return -1
        
    queue.clear()
    queue.append((r,c,cnt))
    
    while queue:
        r,c,cnt = queue.popleft()
        visited2[r][c] = True
        
        if r == e_r and c==e_c:
            r = e_r
            c = e_c
            return cnt
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) and visited2[nr][nc] == False and maps[nr][nc] != 'X':
                queue.append((nr,nc,cnt+1))
                visited2[nr][nc] = True
                
    if(visited2[e_r][e_c]) == False:
        return -1
                
    return -1