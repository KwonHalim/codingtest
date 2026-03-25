def solution(s):
    answer = -1
    idx = 0
    stack = []
    
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1    
