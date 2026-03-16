import sys

input = sys.stdin.readline

def solution(n, roads, costs):

    answer = 0
    curr = 0
    leng = 0
    ncurr=0

    # print(n)
    # print(roads)
    # print(costs)

    while curr<=n-2:
        while True:
            ncurr+=1
            if ncurr>=n-1 or costs[ncurr] < costs[curr]:
                break
        leng=0
        for i in range(curr, ncurr):
            leng+=roads[i]
        answer+=leng*costs[curr]
        curr=ncurr
        
    
    return answer

def main():
    n = int(input().strip())
    roads = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    print(solution(n, roads, costs))

if __name__ == "__main__":
    main()