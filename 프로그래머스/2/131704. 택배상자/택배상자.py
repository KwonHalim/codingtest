from collections import deque

def solution(order):
    answer = 0
    queue = deque([i+1 for i in range(len(order))])
    order_queue = deque(order) 
    li = [0]
    
    while queue:
        box = queue.popleft()
        
        if box != order_queue[0]:
            li.append(box)
        else:
            answer += 1
            order_queue.popleft()
            
        while order_queue and li[-1] == order_queue[0]:
            answer += 1
            order_queue.popleft()
            li.pop()
            
        # print(queue, order_queue)
            
    return answer