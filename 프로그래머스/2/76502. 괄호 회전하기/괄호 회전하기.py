def solution(s):
    answer = 0
    s2 = s*2
    stack = []
    for i in range(len(s)):
        sen = []
        stack = []
        flag = True
        for j in range(len(s)):
            sen.append(s2[i+j])
        # print(sen)
        for k in sen:
            # print(k)
            if k in ['[', '(' ,'{']:
                stack.append(k)
            elif k == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
                    break
            elif k == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
            elif k == '}':
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    flag = False
                    break
        if flag and len(stack) == 0:
            answer+=1
        else:
            pass
        
            
    return answer