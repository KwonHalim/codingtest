def solution(board, moves):
    answer = 0
    stack = []
    row = len(board)
    col = len(board[0])
    for i in range(len(moves)):
        moves[i] = moves[i]-1
    
        
#     i변수는 크레인의 col위치
    for i in moves:
        for j in range(row):
            if board[j][i] != 0:
                break

        doll = board[j][i]
        
        if doll == 0:
            continue
        else:
            board[j][i] = 0
        
        # print(j,i, doll)
        if doll == 0:
            continue
        else:
            if len(stack) != 0 and doll == stack[-1]:
                # print(doll)
                stack.pop()
                answer+=2
            else:
                stack.append(doll)
        
        # print(board, stack)
    return answer