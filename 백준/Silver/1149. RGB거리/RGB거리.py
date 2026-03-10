import sys
input = sys.stdin.readline


def solution(costs):
    for i in range(len(costs)):
        for j in range(3):
            if i == 0:
                continue
            else:
                if j == 0:
                    # print(i, j, min(costs[i-1][1], costs[i-1][2]))
                    costs[i][j] += min(costs[i-1][1], costs[i-1][2])
                elif j == 1:
                    # print(i, j, min(costs[i-1][0], costs[i-1][2]))
                    costs[i][j] += min(costs[i-1][0], costs[i-1][2])
                else:
                    # print(i, j, min(costs[i-1][0], costs[i-1][1]))
                    costs[i][j] += min(costs[i-1][0], costs[i-1][1])
    
    return min(costs[-1])


if __name__ == "__main__":
    n = int(input())
    
    costs = []
    for _ in range(n):
        r, g, b = map(int, input().split())
        costs.append([r, g, b])
    
    result = solution(costs)
    print(result)