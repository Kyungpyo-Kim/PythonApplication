import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]

inf = int(1e9)
distance = [inf for _ in range(v+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

stack = [k]
distance[k] = 0
pq = []
heapq.heappush(pq, (0, k))
while pq:
    cost, pos = heapq.heappop(pq)
    if distance[pos] < cost:
        continue

    for v, w in graph[pos]:
        new_cost = cost + w
        if new_cost < distance[v]:
            distance[v] = new_cost
            heapq.heappush(pq, (new_cost, v))

for dist in distance[1:]:
    print(dist if dist < inf else "INF")    