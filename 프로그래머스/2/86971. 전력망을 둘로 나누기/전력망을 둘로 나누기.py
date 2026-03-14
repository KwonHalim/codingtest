def solution(n, wires):
    
    answer = 1234567890
    
    def dfs(start, graph, visited):
        visited[start] = True
        for con in graph[start]:
            if visited[con] == False:
                dfs(con, graph, visited)
                

    for i in range(len(wires)):
        graph = [[] for j in range(n+1)]
        visited = [False for j in range(n+1)]
        cnt = 0
        for k in range(len(wires)):
            if k == i:
                continue
            a = wires[k][0]
            b = wires[k][1]
            
            graph[a].append(b)
            graph[b].append(a)
        dfs(1, graph, visited)
        
        for i in range(1,len(visited)):
            if (visited[i] == True):
                cnt+=1
                
                
        answer = min(answer, abs(cnt - (n - cnt)))
            
    return answer