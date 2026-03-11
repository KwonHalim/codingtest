import sys
input = sys.stdin.readline


def solution(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))

    end_time = 0
    count = 0

    for start, end in meetings:
        if start >= end_time:
            count+=1
            end_time = end

    return count


if __name__ == "__main__":
    n = int(input())

    meetings = []
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))

    result = solution(meetings)
    print(result)