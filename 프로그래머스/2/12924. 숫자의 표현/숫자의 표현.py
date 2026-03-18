def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        num = i+1
        result = i
        while True:
            # print("i", i, "result", result, "num", num)
            result+=num
            if result == n:
                answer+=1
                # print("m")
                break
            elif result < n:
                num+=1
            else:
                break
    
            
    return answer+1