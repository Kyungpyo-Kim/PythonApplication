"""

1. idea
- N, L, R
- BFS 로 합칠 나라 모으기
- 조건대로 맵 업데이트

2. complexity

3. data structure

4. category
- BFS

"""

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [[0] * N for _ in range(N)]
starts = []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        graph[i][j] = v
        starts.append((i, j))


def check(x, y):
    for dx, dy in zip(dys, dxs):
        nx = x + dx
        ny = y + dy
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                return 0
    return 1


dxs = (-1, 0, 1, 0)
dys = (0, -1, 0, 1)
cnt = 0
q = deque()
while True:
    visited = set()
    merged = []
    sums = []
    update = False

    for start in starts:
        m = []
        q.append(start)
        s = 0

        while q:
            x, y = q.popleft()

            if check(x, y) == 1:
                visited.add((x, y))
                continue

            if (x, y) not in visited:
                visited.add((x, y))

                m.append((x, y))
                s += graph[x][y]
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                        if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                            q.append((nx, ny))

        if len(m) > 1:
            s = s // len(m)
            for x, y in m:
                graph[x][y] = s

            update = True

    if update:
        cnt += 1
    else:
        break

print(cnt)
