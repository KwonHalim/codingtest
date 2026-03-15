import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    visited = [[False for i in range(len(maps[0]))]for i in range(len(maps))]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    cnt=0
    
    
    def dfs(r,c):
        visited[r][c] = True
        cnt = int(maps[r][c])
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) and not visited[nr][nc] and maps[nr][nc] != 'X':
                result=dfs(nr,nc)
                cnt += result
        return cnt

        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] !='X' and not visited[i][j]:
                result = dfs(i,j)
                answer.append(result)

    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
        
        
    return answer