n, m = map(int, input().split())
graph = []
# 상,하,좌,우
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

# graph변수에는 0,1로 이루어진 지도가 들어가 있는 상태
for _ in range(n):
    one_line = input()
    line = list(map(int, list(one_line)))
    graph.append(line)

visited = [[0] * (m) for i in range(n)]
count = [[0] * (m) for i in range(n)]


def bfs(x, y):
    queue = []
    queue.append((x, y))
    visited[x][y] = 1
    count[x][y] = 1
    while (queue):
        x, y = queue.pop(0)
        for i in range(4):
            mx = x + move_x[i]
            my = y + move_y[i]
            if ((0 <= mx < n) and (0 <= my <m) and visited[mx][my] == 0) and (graph[mx][my] == 1):
                queue.append((mx, my))
                visited[mx][my] = 1
                count[mx][my] = count[x][y] + 1



bfs(0, 0)
print(count[n - 1][m - 1])

