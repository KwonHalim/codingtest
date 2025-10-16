from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
#     상,하,좌,우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
#     x,y,cnt
    queue = deque([(0, 0, 1)])
    
    visited[0][0] = True
    
    while queue:
        y, x, cost = queue.popleft()
        
        if y == n - 1 and x == m - 1:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True 
                    queue.append((ny, nx, cost + 1)) 
                    
    return -1