from collections import Counter

def solution(topping):
    answer = 0
    
    right = Counter()
    left = Counter(topping)
    # print(left)
    # print(len(left))
    
    for t in topping:
        if t in left:
            left[t] -=1
        if left[t] == 0:
            del left[t]
        if t in right:
            right[t] +=1
        else:
            right[t] =1        
        if len(left) == len(right):
            answer+=1

            
    return answer