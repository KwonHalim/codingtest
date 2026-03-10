import sys
from collections import deque

input = sys.stdin.readline


def solution(m, n, box):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]


    queue = deque()
    cnt = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append([i,j])


    while queue:
        li = []
        while queue:
            x,y = queue.pop()
            li.append([x,y])
        for x,y in li:
            for i in range(4):
                if 0<=x+dx[i]<=(n-1) and 0<=y+dy[i]<=(m-1) and box[x+dx[i]][y+dy[i]] == 0:
                    queue.append([x+dx[i],y+dy[i]])
                    box[x+dx[i]][y+dy[i]] = 1

        cnt+=1


    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1

    return cnt-1


if __name__ == "__main__":
    m, n = map(int, input().split())

    box = []
    for _ in range(n):
        row = list(map(int, input().split()))
        box.append(row)

    result = solution(m, n, box)
    print(result)