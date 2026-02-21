def solution(players, m, k):
    n = len(players)
    server = [0] * (n+k) #구동중인 서버 개수
    count = 0
    
    
    for i in range(n):
        if(players[i] < (server[i] + 1) * m):
            continue
        else:
            now = server[i] * m
            need = (players[i] - now) // m
            count = count + need
            for j in range(k):
                server[i+j] = server[i+j] + need
            
            
    

    return count