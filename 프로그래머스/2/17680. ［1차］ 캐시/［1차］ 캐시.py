from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    
    queue = deque()
    
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            return len(cities) * 5
        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer+=1
        elif len(queue) < cacheSize:
            queue.append(city)
            answer+=5
        else:
            queue.popleft()
            queue.append(city)
            answer+=5
        # print(queue)
        # print(answer)
    
    return answer