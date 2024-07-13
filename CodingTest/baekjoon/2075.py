"""

1. idea
- priority queue 에 그냥 크기 조절하면서 넣기

2. complexity
- time: N

3. data structure
- heapq

4. category
- heapq

"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())

q = []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        heapq.heappush(q, v)
        if len(q) > N:
            heapq.heappop(q)

print(heapq.heappop(q))
