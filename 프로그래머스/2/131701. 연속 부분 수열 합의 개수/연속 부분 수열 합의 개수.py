from itertools import combinations

def solution(elements):
    answer = 0
    
    s = set()
    for i in range(len(elements)):
        sum = 0
        idx = 0
        for j in range(len(elements)):
            if i+j >= len(elements):
#                 i = 3, j = 0,1,2 -> 3번부터 (3번위치,4번위치,0번위치)
                idx = (i+j) % len(elements)
            else:
                idx = i + j
            sum+=elements[idx]
            s.add(sum)
            # print(i,j, idx, sum)
    # print(s)
        
    return len(s)