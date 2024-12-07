"""
rotate 하는 r 을 받으면, 현재 x, y 에서 r 만큼 움직인 x, y 를 계산해낼 수 있음

1 2 5 3 4
5 6 6 7 8
9 1 7 1 1
1 1 5 8 6

1 2 3 4
5 6 7 8
1 1 8 6
1 1 8 6
1 1 8 6

같은 Line 을 빼서 r 만큼 돌려놓고 다시 사각형으로 그리기?
line 갯수는 min(n//2, m//2)

rect to line
len = 2n + 2m - 4


x, y = 0, 0
for i in range(len):
    line.append(rect[x, y])
    if x < n - 1:
        x += 1
    elif x == n-1 and y < m - 1:
        y += 1
    elif x > 0 and y == m - 1:
        x -= 1
    elif x == 0 and y > 0:
        y -= 1

"""

import sys

input = sys.stdin.readline

n, m, r = map(int, input().strip().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().strip().split())))


def rotate(board, r):
    n, m = len(board), len(board[0])
    l = min(n, m) // 2
    for i in range(l):
        c = []
        c_len = 2 * (n - 2 * i) + 2 * (m - 2 * i) - 4
        x, y = i, i
        for _ in range(c_len):
            c.append(board[x][y])
            if x < n - 1 - i and y == i:
                x += 1
            elif x == n - 1 - i and y < m - 1 - i:
                y += 1
            elif x > i and y == m - 1 - i:
                x -= 1
            elif x == i and y > i:
                y -= 1

        # print(i, *c)

        _r = r % c_len

        def reverse(start, end):
            while start < end:
                c[start], c[end] = c[end], c[start]
                start += 1
                end -= 1

        reverse(0, c_len - 1)
        reverse(0, _r - 1)
        reverse(_r, c_len - 1)

        # print(i, *c)

        x, y = i, i
        for j in range(c_len):
            board[x][y] = c[j]
            if x < n - 1 - i and y == i:
                x += 1
            elif x == n - 1 - i and y < m - 1 - i:
                y += 1
            elif x > i and y == m - 1 - i:
                x -= 1
            elif x == i and y > i:
                y -= 1

    return board


board = rotate(board, r)

for b in board:
    print(*b)


"""해설 코드, 시간 초과...

import sys

input = sys.stdin.readline

N, M, R = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(N)]

sr, sc = 0, 0
n, m = N, M

a_iter = min(N, M) // 2

for _ in range(a_iter):

    a_len = 2 * (n + m - 2)
    r = R % a_len

    for _ in range(r):
        tmp = A[sr][sc]

        r, c = sr, sc

        for dr, dc in zip([0, 1, 0, -1], [1, 0, -1, 0]):

            dist = n - 1 if dr != 0 else m - 1

            for _ in range(dist):
                A[r][c] = A[r + dr][c + dc]
                r, c = r + dr, c + dc

        A[sr + 1][sc] = tmp

    sr, sc = sr + 1, sc + 1
    n, m = n - 2, m - 2

for a in A:
    print(*a)
"""
