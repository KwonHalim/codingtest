import sys

input = sys.stdin.readline

def solution(n, balls):
    answer= 0

    red = balls.count('R')
    blue = n - red

    left_red = 0
    right_red = 0

    left_blue = 0
    right_blue = 0

    for i in range(-1,-n,-1):
        if balls[i] == 'B':
            break
        right_red+=1
    
    for i in range(-1,-n,-1):
        if balls[i] == 'R':
            break
        right_blue+=1
        

    for i in range(n):
        if balls[i] == 'B':
            break
        left_red+=1


    for i in range(n):
        if balls[i] == 'R':
            break
        left_blue+=1

    answer = min(red - left_red, red-right_red, blue-right_blue, blue-left_blue)



    return answer

def main():
    n = int(input().strip())
    balls = input().strip()
    print(solution(n, balls))

if __name__ == "__main__":
    main()