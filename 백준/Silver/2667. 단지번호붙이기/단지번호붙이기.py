import sys

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

size = [] 
dw = [0, 0, -1, 1]
dh = [1, -1, 0, 0]

def dfs(i, j, grid, visited):
    if i >= n or j >= n or i < 0 or j < 0:
        return 0
    
    if visited[i][j] == False and grid[i][j] == 1:
        visited[i][j] = True
        num = 1 
        
        for k in range(4):
            num += dfs(i + dw[k], j + dh[k], grid, visited)
        return num
    return 0

def solution(n, grid):
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                result = dfs(i, j, grid, visited)
                if result > 0:
                    size.append(result)
    
    size.sort()
    print(len(size))
    for s in size:
        print(s)

solution(n, grid)