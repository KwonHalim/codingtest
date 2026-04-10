def solution(park, routes):
    answer = []
    c_row = 0
    c_col = 0
    n_row = 0
    n_col = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                c_row = i
                c_col = j
                break

    
    for r in routes:
        d, l = r.split(" ")
        l = int(l)
        n_row,n_col = c_row,c_col
        if d == 'N': #북, 위쪽
            for i in range(l):
                n_row = n_row -1
                if n_row < 0 or n_row >=len(park) or n_col <0 or n_col >= len(park[0]) or park[n_row][n_col] == 'X':
                    break
            else:
                c_row, c_col = n_row, n_col
        elif d == 'S': #남, 아래쪽
            for i in range(l):
                n_row = n_row +1
                if n_row < 0 or n_row >=len(park) or n_col <0 or n_col >= len(park[0]) or park[n_row][n_col] == 'X':
                    break
            else:
                c_row, c_col = n_row, n_col
        elif d == 'W': #서, 왼쪽
            for i in range(l):
                n_col = n_col -1
                if n_row < 0 or n_row >=len(park) or n_col <0 or n_col >= len(park[0]) or park[n_row][n_col] == 'X':
                    break
            else:
                c_row, c_col = n_row, n_col
        else: #동, 오른쪽
            for i in range(l):
                n_col = n_col + 1
                if n_row < 0 or n_row >=len(park) or n_col <0 or n_col >= len(park[0]) or park[n_row][n_col] == 'X':
                    break
            else:
                c_row, c_col = n_row, n_col
                
    return [c_row,c_col]