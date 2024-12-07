import sys

input = sys.stdin.readline

N, k = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))


dxdys = {
    0: ((1, 0), (0, 1)),
    1: ((0, -1), (1, 0)),
    2: ((-1, 0), (0, 1)),
    3: ((0, -1), (-1, 0)),
    4: ((-1, 0), (1, 0)),
    5: ((0, -1), (0, 1)),
}


def solve():
    x, y = 0, -1
    gx, gy = N - 1, N
    dx, dy = 0, 1
    dist = 0
    while True:
        print("move: ", dist, x, y, dx, dy)

        # check availablity
        nx, ny = x + dx, y + dy

        dxdy = dxdys[board[nx][ny]]
        # print(board[nx][ny], dxdy)

        if (x - nx, y - ny) in dxdy:
            dx, dy = dxdy[0] if dxdy[0] == (x - nx, y - ny) else dxdy[1]
            x, y = nx, ny
        else:
            return -1

        dist += 1

        if x == gx and y == gy:
            return dist

        if (not (0 <= x < N)) or (not (0 <= y < N)):
            return -1


if k == 0:
    print(solve())
else:
    dist = -1
    for i in range(N):
        for j in range(N):
            a = board[i][j]
            for k in range(6):
                if a != k:
                    print("test: ", i, j, k)
                    board[i][j] = k
                    dist = max(dist, solve())
            board[i][j] = a

    print(dist)
