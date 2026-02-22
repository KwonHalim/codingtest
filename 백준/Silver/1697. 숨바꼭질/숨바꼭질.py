from collections import deque

a, b = map(int, input().split())

deq = deque()

def bfs(a, b):
    visited = [-1] * 200001
    visited[a] = 0
    deq.append(a)
    while (deq):
        curr = deq.popleft()
        if (curr == b):
            return visited[b]
        if (curr + 1 <= 100000 and visited[curr + 1] == -1):
            visited[curr + 1] = visited[curr] + 1
            deq.append(curr + 1)
        if (curr - 1 >= 0 and visited[curr - 1] == -1):
            visited[curr - 1] = visited[curr] + 1
            deq.append(curr - 1)
        if (curr * 2 <= 100000 and visited[curr * 2] == -1):
            visited[curr * 2] = visited[curr] + 1
            deq.append(curr * 2)


ans = bfs(a,b)
print(ans)