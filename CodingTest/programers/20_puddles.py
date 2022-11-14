# 프로그래머스 레벨3 등굣길 동적계획법
from collections import deque


def solution(m, n, puddles):
    dist_table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    for x, y in puddles:
        visited[y][x] = True

    start = (1, 1)

    dist_table[start[0]][start[1]] = 1
    visited[start[0]][start[1]] = True
    q = deque([start])
    while q:
        cur = q.popleft()
        next = [(cur[0] + 1, cur[1]), (cur[0], cur[1] + 1)]
        for x, y in next:
            if x <= n and y <= m and not visited[x][y]:
                dist_table[x][y] += dist_table[x - 1][y]
                dist_table[x][y] += dist_table[x][y - 1]
                visited[x][y] = True
                q.append((x, y))

    return dist_table[n][m] % 1000000007

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))
