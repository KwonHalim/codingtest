from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    add=sum1+sum2
    q1 = deque()
    q2 = deque()
    count = 0
    for i in queue1:
        q1.append(i)
    for i in queue2:
        q2.append(i)
    sumq1 = sum(q1)
    while(True):
        if(sumq1 == add/2):
            break
        if(sumq1< add/2):
            num = q2.popleft()
            q1.append(num)
            sumq1=sumq1+num
        elif(sumq1 > add/2):
            num = q1.popleft()
            q2.append(num)
            sumq1=sumq1-num
        count+=1

        if(count>1234567):
            return -1
    return count