def solution(numbers, target):
    def dfs(idx,target,result):
        if result == target and idx == len(numbers):
            return 1
        elif idx == len(numbers) and result != target:
            return 0
        
        return dfs(idx+1,target, result + numbers[idx]) + dfs(idx+1,target, result - numbers[idx])
        
    answer = dfs(0,target,0)
    return answer
