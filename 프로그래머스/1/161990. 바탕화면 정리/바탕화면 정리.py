def solution(wallpaper):
    answer = [0 for i in range(4)]
    big_col = -1
    small_col = float('inf')
    big_row = -1
    small_row = float('inf')
    for j,row in enumerate(wallpaper):
        # print(row)
        for i,col in enumerate(row):
            if col == '#':
                if j > big_row:
                    big_row = j
                if j < small_row:
                    small_row = j
                # print(j)
                if int(i) > big_col:
                    big_col = i
                if i < small_col:
                    small_col = i
    # print(big,small)
    answer[3] = big_col+1
    answer[1] = small_col
    answer[0] = small_row
    answer[2] = big_row+1
    
    return answer