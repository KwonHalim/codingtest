import sys
from collections import deque
sys.setrecursionlimit(10**6)

def solution(n, wires):
    ##DFS##
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    parent = [0]*(n+1)

    parent[1] = 1

    def dfs(start):
        for i in graph[start]:
            if parent[i] == 0:
                parent[i] = start
                dfs(i)
    dfs(1)
    for i in range(2, n + 1):
        print(parent[i])
'''
##BFS##
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

    parent = [0] * (n+1)

    queue = deque()

    queue.append(1)

    parent[1] = 1

    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if parent[i] == 0:
                parent[i] = curr
                print(parent)
                queue.append(i)

    for i in range(2, n + 1):
        print(parent[i])

'''







# 한 줄씩 읽기
line = sys.stdin.readline()
if not line:
    sys.exit()

n = int(line.strip())
wires = []

for _ in range(n - 1):
    edge = list(map(int, sys.stdin.readline().split()))
    if edge:
        wires.append(edge)

solution(n, wires)