"""

1. idea
- simulation
    - 구슬 움직이기
        - 움직이는 방향으로 스캔
        - 구슬이 있으면 움직여 놓기
        - 구슬이 2개 다 움직이지 않았으면 끝까지 확인
        - 구슬 position 을 저장해서 handling 하기 -> x
- BFS 로 최소 step 을 찾기
    - 움직일 수 있는지 체크

2. complexity

3. data structure

"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [[None] * M for _ in range(N)]
rx, ry = 0, 0
bx, by = 0, 0
ox, oy = 0, 0

for i in range(N):
    row = input()
    for j in range(M):
        board[i][j] = row[j]
        if row[j] == "R":
            rx, ry = i, j
        if row[j] == "B":
            bx, by = i, j
        if row[j] == "O":
            ox, oy = i, j


def move(x, y, dx, dy):
    nx, ny = x, y
    while 1 <= nx <= N - 2 and 1 <= ny <= M - 2:
        if board[nx + dx][ny + dy] == "#":
            break
        else:
            nx += dx
            ny += dy
    return nx, ny


dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]
