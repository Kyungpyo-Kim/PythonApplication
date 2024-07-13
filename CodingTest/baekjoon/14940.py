"""

1. idea
- BFS 

2. complexity


3. data structure
- 2d list

4. category
- BFS
- Backtracking


"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

table = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v == 2:
            x, y = i, j
        if v != 0:
            table[i][j] = -1

dxs = (+1, -1, 0, 0)
dys = (0, 0, +1, -1)

q = deque([[x, y, 0]])

while q:
    x, y, dist = q.popleft()
    if table[x][y] == -1:
        table[x][y] = dist

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                q.append([nx, ny, dist + 1])

for t in table:
    print(*t)
