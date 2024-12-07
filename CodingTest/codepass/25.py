"""

찾는 방향: 가로, 세로, 대각 업, 대각 다운
찾기 시작 전에 연속된 방향 없어야 함

"""

import sys

input = sys.stdin.readline

board = [[0] * 19 for _ in range(19)]

for x in range(19):
    for y, v in enumerate(map(int, input().strip().split())):
        board[x][y] = v


def get_seq_len(x, y, dx, dy):
    seq_len = 1
    g = board[x][y]
    if 0 <= x - dx < 19 and 0 <= y - dy < 19:
        if board[x - dx][y - dy] == g:
            return 0

    while True:
        x, y = x + dx, y + dy
        if 0 <= x < 19 and 0 <= y < 19 and board[x][y] == g:
            seq_len += 1
        else:
            break
    return seq_len


def find_winner():
    g, r, c = 0, 0, 0
    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                for dx, dy in zip([1, 0, 1, -1], [0, 1, 1, 1]):
                    if get_seq_len(x, y, dx, dy) == 5:
                        return board[x][y], x + 1, y + 1
    return 0, 0, 0


g, r, c = find_winner()

print(g)
if g:
    print(r, c)
