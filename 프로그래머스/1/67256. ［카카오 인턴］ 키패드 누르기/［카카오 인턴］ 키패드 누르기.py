def solution(numbers, hand):
    answer = ''
    li = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    
    left = (3,0)
    right = (3,2)
    
    for number in numbers:
        if number in [1,4,7]:
            if number == 1:
                left = li[1]
            elif number == 4:
                left = li[4]
            else:
                left = li[7]
            answer+='L'
                
        elif number in [3,6,9]:
            if number == 3:
                right = li[3]
            elif number == 6:
                right = li[6]
            else:
                right = li[9]
            answer+='R'
            
        else:
            row,col = li[number]
            right_row,right_col = right
            left_row,left_col = left
            
            left_dist = abs(left_row - row) + abs(left_col - col)
            right_dist = abs(right_row - row) + abs(right_col - col)
            
            if left_dist < right_dist:
                left = (row,col)
                answer+='L'
            elif left_dist > right_dist:
                right = (row,col)
                answer+='R'
            elif left_dist==right_dist:
                if hand == 'right':
                    right = (row,col)
                    answer+='R'
                else:
                    left = (row,col)
                    answer+='L'
            
    return answer