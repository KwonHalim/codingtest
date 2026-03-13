def solution(A, B):
    result = 0

    def dfs(A, B):

        if A==B:
            return 1
        if A>B:
            return -1
        
        if B % 10 == 1:
            value = dfs(A,B // 10)
            if value != -1:
                return value + 1

        if B % 2 == 0:
            value = dfs(A,B // 2)
            if value != -1:
                return value + 1
            
        
        return -1
        

    result = dfs(A, B)
    return result


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(solution(A, B))