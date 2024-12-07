"""

숫자 하나 나오면,
그 숫자 주변으로 빙고가 생기는지 확인
생겼으면 cnt 증가
3개 되면 break

"""

import sys

input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(5)]
say = []
for _ in range(5):
    say += list(map(int, input().strip().split()))

pos = {}
for x in range(5):
    for y in range(5):
        pos[board[x][y]] = (x, y)


def find_bingo(x, y):
    bingo = 0

    is_bingo = True
    for i in range(5):
        if board[x][y] != board[x][i]:
            is_bingo = False
            break
    bingo += 1 if is_bingo else 0

    is_bingo = True
    for i in range(5):
        if board[x][y] != board[i][y]:
            is_bingo = False
            break
    bingo += 1 if is_bingo else 0

    if x == y:
        is_bingo = True
        for i in range(5):
            if board[x][y] != board[i][i]:
                is_bingo = False
                break
        bingo += 1 if is_bingo else 0

    if x + y == 4:
        is_bingo = True
        for i in range(5):
            if board[x][y] != board[4 - i][i]:
                is_bingo = False
                break
        bingo += 1 if is_bingo else 0

    return bingo


cnt, bingo = 0, 0
while cnt < len(say):
    b = say[cnt]
    x, y = pos[b]
    board[x][y] = 0
    bingo += find_bingo(x, y)
    if bingo >= 3:
        break

    cnt += 1

print(cnt + 1)
