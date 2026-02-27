def solution(sequence, k):
    answer = []
    n = len(sequence)
    
    current_sum = 0
    left = 0
    min_len = 1234567890
    
    for right in range(len(sequence)):
        current_sum+=sequence[right]
        while(current_sum>k):
            current_sum-=sequence[left]
            left+=1
            
            
        if(current_sum==k):
            if(right-left+1 < min_len):
                min_len=right-left+1
                answer=[left,right]
    return answer