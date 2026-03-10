import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)
# 각 위치에서 도달할 수 있는 노드, 정점까지의 거리 쌍
# [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
# 위치에서 가는 거리, 정점
#heapq -> (1,2)

dist = [float('INF')] * (V+1)
dist[K] = 0

# 다음에 갈 위치 저장
heap= []

heapq.heappush(heap,(0,K))

while heap:
    print(heap)
    print(dist)
    # distance는 지금까지 node까지의 거리
    distance, node = heapq.heappop(heap)
    if distance > dist[node]:
        continue

    for next_node, weight in graph[node]:
        # 현재(현재(node)의 위치까지의 거리) + next_node까지의 거리 계산
        new_dist = weight + distance
        # 위의 거리가 이미 저장되어있는 거리보다 짧다면 업데이트
        if dist[next_node] > new_dist:
            dist[next_node] = new_dist
            heapq.heappush(heap,(new_dist,next_node))


for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
