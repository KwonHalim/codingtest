import sys


def solution(n, triangle):

    for i in range(1,n):
        for j in range(i+1):
            if(j==0):
                triangle[i][j] += triangle[i-1][j]
            elif(j==i):
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # print(triangle)
    return (max(max(triangle)))

if __name__ == "__main__":
    # 1. 먼저 n을 입력받습니다.
    line = sys.stdin.readline()
    if not line:
        exit()

    n = int(line.strip())
    triangle = []

    # 2. n번만큼만 반복해서 한 줄씩 읽어옵니다.
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        triangle.append(row)

    # 결과 확인
    print(solution(n, triangle))