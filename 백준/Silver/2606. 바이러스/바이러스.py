num = int(input())
pair = int(input())
cnt = 0
arr = [[0] * (num+1) for _ in range(num+1)]
visited = [0] * (num+1)


def bfs(n):
    global cnt
    queue = [n]
    visited[n] = 1
    while queue:
        n = queue.pop(0)
        for i in range(num+1):
            if arr[n][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                cnt += 1


for i in range(pair):
    n, m = map(int, input().split())
    arr[n][m] = arr[m][n] = 1



bfs(1)

print(cnt)