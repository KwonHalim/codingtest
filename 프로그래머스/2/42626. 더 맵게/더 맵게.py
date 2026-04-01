import heapq

def solution(scoville, K):
    
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    sco = -1
    cnt = 0
    while True:
        
        if len(heap) < 2 and heap[0] <= K:
            return -1
        
        if heap[0] >= K:
            return cnt
        
        m1 = heapq.heappop(heap)
        m2 = heapq.heappop(heap)

        
        sco = m1 + m2*2
        cnt+=1
        heapq.heappush(heap, sco)
        # print(heap)
    
    return cnt