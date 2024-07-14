"""

1. idea
- N (100,000), K (100,000)
- x+1, x-1, 2x -> graph 로 치환
- 1, 1, 0 -> 다른 가중치 사용 -> Dijkstra algorithm

2. complexity
- Dijkstra algorithm: VlogV + ElogV -> NlogN

3. data structure
- list

4. category
- Dijkstra

"""

import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

INF = 10**7
n_max = 100001
d = [INF for _ in range(n_max)]
d[N] = 0
visited = [0 for _ in range(n_max)]

q = []
heapq.heappush(q, (0, N))

while q:
    dist, position = heapq.heappop(q)
    if visited[position] == 0:
        visited[position] = 1
        next_pos = (position - 1, position + 1, 2 * position)
        next_weight = (1, 1, 0)
        for p, w in zip(next_pos, next_weight):
            if 0 <= p < n_max:
                d[p] = min(d[p], d[position] + w)
                heapq.heappush(q, (d[p], p))

print(d[K])
