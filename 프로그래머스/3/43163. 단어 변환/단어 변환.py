from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = [False] * len(words)
    
    while queue:
        start, cnt = queue.popleft()
        if start == target:
            return cnt
        
        for i, next_word in enumerate(words):
            if visited[i] == True:
                continue
                
            diff = 0
            for j in range(len(start)):
                if start[j] != next_word[j]:
                    diff+=1
                
            if diff==1:
                visited[i] = True
                queue.append((next_word, cnt+1))
    return 0