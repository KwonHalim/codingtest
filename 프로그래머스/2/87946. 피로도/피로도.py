def solution(k, dungeons):
    answer = -1
    
    visited = [False for i in range(len(dungeons))]
    
    def dfs(current_k,cnt):
        nonlocal answer
        answer = max(answer,cnt)
        for i in range(len(dungeons)):
            if visited[i] == False and dungeons[i][0] <= current_k:
                visited[i] = True
                dfs(current_k - dungeons[i][1],cnt+1)
                visited[i] = False
    
    
    dfs(k,0)
        
    
    return answer