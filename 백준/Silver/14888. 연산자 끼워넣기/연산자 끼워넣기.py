import sys
input = sys.stdin.readline


def solution(numbers, operators):

    def dfs(idx, val, plus, minus, mul, div):

        max_value = float('inf') * -1
        min_value = float('inf')    

        if idx == len(numbers):
            return val, val
        
        if plus > 0:            
            val1, val2= dfs(idx+1, val + numbers[idx], plus-1, minus, mul, div)
            max_value = max(max_value, val1)
            min_value = min(min_value, val2)

        if minus > 0:
            val1, val2 = dfs(idx+1, val - numbers[idx] , plus, minus-1, mul, div)
            max_value = max(max_value, val1)
            min_value = min(min_value, val2)

        if mul > 0:
            val1, val2 = dfs(idx+1, val * numbers[idx] , plus, minus, mul-1, div)
            max_value = max(max_value, val1)
            min_value = min(min_value, val2)

        if div > 0:
            val1, val2 = dfs(idx+1, int(val / numbers[idx]), plus, minus, mul, div-1)
            max_value = max(max_value, val1)
            min_value = min(min_value, val2)
        
        return max_value, min_value
    

    return dfs(1,numbers[0],operators[0],operators[1],operators[2],operators[3])



if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    max_value, min_value = solution(numbers, operators)
    print(max_value, min_value)