"""

1. idea
- DFS 로 완전 탐색하고 가능한 케이스가 생기는지 확인
2. complexity
3. data structure
4. category

"""

import sys

input = sys.stdin.readline


def check(board):
    # 1행, 2행, 3행
    if board[0] == board[1] == board[2] != -1:
        return True
    if board[3] == board[4] == board[5] != -1:
        return True
    if board[6] == board[7] == board[8] != -1:
        return True
    # 1열, 2열, 3영
    if board[0] == board[3] == board[6] != -1:
        return True
    if board[1] == board[4] == board[7] != -1:
        return True
    if board[2] == board[5] == board[8] != -1:
        return True
    # 대각선 2개
    if board[0] == board[4] == board[8] != -1:
        return True
    if board[6] == board[4] == board[2] != -1:
        return True
    return False


def play(board, xs, os, x_first):
    if len(xs) == len(os) == 0:
        if -1 not in board:
            return True
        else:
            if check(board):
                return True
            else:
                return False

    if check(board):
        return False

    if x_first:
        for i in range(len(xs)):
            board[xs[i]] = 1
            nxs = xs[:i] + xs[i + 1 :]
            if play(board, nxs, os, False):
                return True
            board[xs[i]] = -1

    else:
        for i in range(len(os)):
            board[os[i]] = 0
            nos = os[:i] + os[i + 1 :]
            if play(board, xs, nos, True):
                return True
            board[os[i]] = -1

    return False


while True:
    ttt = input().strip()
    if ttt == "end":
        break

    xs = []
    os = []
    for i, t in enumerate(list(ttt)):
        if t == "X":
            xs.append(i)
        if t == "O":
            os.append(i)

    board = [-1] * 9
    game = play(board, xs, os, True)
    print("valid" if game else "invalid")
