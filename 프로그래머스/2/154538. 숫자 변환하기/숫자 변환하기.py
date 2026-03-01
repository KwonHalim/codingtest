from collections import deque
def solution(x, y, n):    
    answer = [-1] * ((y*3))
    
    queue = deque()
    
    queue.append((x,0))
        
    while queue:
        a,b = queue.popleft()
        if(answer[a] == -1):
            answer[a]=b
            if(a+n <= y):
                queue.append((a+n,b+1))
            if(a*2 <= y):
                queue.append((a*2,b+1))
            if(a*3 <= y):
                queue.append((a*3,b+1))
        if(a==y):
            return answer[a]
                
    return -1