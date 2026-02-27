def solution(book_time):
    times = []
    for start, end in book_time:
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        times.append([s_h * 60 + s_m, e_h * 60 + e_m + 10])
    
    times.sort()
    
    print(times)
    
    rooms = [] #끝나는 시간 저장
    
    for start,end in times:
        found = False
        for i in range(len(rooms)):
            if(rooms[i] <= start):
                rooms[i]=end
                found=True
                break
                
        if not found:
            rooms.append(end)
            
            
    return len(rooms)