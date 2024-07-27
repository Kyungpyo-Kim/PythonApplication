"""

1. idea
- N: 50,000
- M: 50,000
- Dijkstra 로 최소 비용 그래프 탐색
- C >= 0
- 양방향 그래프 추가

2. complexity
- time: VlogV + ElogV -> NlogN + MlogN ~= NlogN

3. data structure
- 2d list for graph
- heapq

4. category
- Dijkstra

"""

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1000 * 50000

graph = defaultdict(list)
d = [INF] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

hq = []
d[1] = 0
heapq.heappush(hq, (d[1], 1))

while hq:
    cost, pos = heapq.heappop(hq)
    if not visited[pos]:
        visited[pos] = 1
        for next_cost, next_pos in graph[pos]:
            d[next_pos] = min(d[next_pos], cost + next_cost)
            heapq.heappush(hq, (d[next_pos], next_pos))

print(d[N])
