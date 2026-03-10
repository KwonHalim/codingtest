import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)



def solution(n, edges):



    edges.sort()
    graph = [[] for i in range(n+1)]
    for start,end in edges:
        graph[start].append(end)
        graph[end].append(start)


    visited = [False for i in range(n+1)]

    def dfs(start):
        visited[start] = True
        for v in graph[start]:
              if visited[v] == False:
                dfs(v)

    answer = 0
    for i in range(1,n+1):
        if visited[i] == False:
            answer+=1
            dfs(i)
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = solution(n, edges)
    print(result)