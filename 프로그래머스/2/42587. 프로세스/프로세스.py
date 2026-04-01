from collections import deque

def solution(priorities, location):
    answer = 0
# A,B,C,D
# 2 1 3 2
# C D A B
# 1 2 3 4
    queue = deque()
    idx = 0
    for i in priorities:
        queue.append((i,idx))
        idx+=1
    # print(queue)
        
    cnt = 0
    while queue:
        m = -1
        for i in queue:
            if m < i[0]:
                m = i[0]
        # print(m)
        num, idx = queue.popleft()
        if num == m:
            cnt+=1
            if idx == location:
                return cnt
            else:
                continue            
        else:
            queue.append((num,idx))
        # print(queue)

    return answer