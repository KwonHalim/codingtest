def solution(dirs):
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    x,y = 0,0

    path = []
    
    for i in dirs:
        if i == "U":
            nx = x + dr[0]
            ny = y + dc[0]
            if -5<=nx<=5 and -5<=ny<=5: 
                mv = ((x,y),(nx,ny))
                move = sorted(mv)
                if move not in path:    
                    path.append(move)
                x,y = nx,ny
        elif i == "D":
            nx = x + dr[1]
            ny = y + dc[1]
            if -5<=nx<=5 and -5<=ny<=5: 
                mv = ((x,y),(nx,ny))
                move = sorted(mv)
                if move not in path:    
                    path.append(move)
                x,y = nx,ny
        elif i == "L":
            nx = x + dr[2]
            ny = y + dc[2]
            if -5<=nx<=5 and -5<=ny<=5: 
                mv = ((x,y),(nx,ny))
                move = sorted(mv)
                if move not in path:    
                    path.append(move)
                x,y = nx,ny
        else:
            nx = x + dr[3]
            ny = y + dc[3]
            if -5<=nx<=5 and -5<=ny<=5: 
                mv = ((x,y),(nx,ny))
                move = sorted(mv)
                if move not in path:    
                    path.append(move)
                x,y = nx,ny
    
    
    return len(path)