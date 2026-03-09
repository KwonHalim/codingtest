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
dist = [INF] * (V + 1)
dist[K] = 0

# print(graph)

heap = []
# heap: 해당노드까지의 거리, 도착노드
heapq.heappush(heap,(0,K))
# Grpah는 노드, 거리 순

while heap:
    distance, node = heapq.heappop(heap)
    if distance > dist[node]:
        continue

    for new_node, weight in graph[node]:
        new_dist = weight + distance

        if new_dist < dist[new_node]:
            dist[new_node] = new_dist
            heapq.heappush(heap,(new_dist, new_node))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])