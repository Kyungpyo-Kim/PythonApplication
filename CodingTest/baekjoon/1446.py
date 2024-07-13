"""

1. idea
- N, D
- 1 ~ N 까지 거리 채우고
- 지름길기준으로 최소 거리 수정, 이후에 다 반영
- end key 로 dict 만들어서 거리 체크에 사용

2. complexity
- time: N

3. data structure
- list
- dict

4. category
- DP or dijkstra

"""

import sys

input = sys.stdin.readline

N, D = map(int, input().split())
shortcuts = {}
for _ in range(N):
    start, end, dist = map(int, input().split())
    if end not in shortcuts:
        shortcuts[end] = []
    shortcuts[end].append((start, dist))

dist_list = [0 for _ in range(D + 1)]
for i in range(1, D + 1):
    dist = dist_list[i - 1] + 1
    if i in shortcuts:
        for s, d in shortcuts[i]:
            dist = min(dist_list[s] + d, dist)
    dist_list[i] = dist

print(dist_list[D])
