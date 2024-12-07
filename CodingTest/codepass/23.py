import sys

input = sys.stdin.readline

N = int(input())

board = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().strip().split())
    for i in range(10):
        for j in range(10):
            board[x + i][y + j] = 1

cnt = 0

for x in range(100):
    for y in range(100):
        if board[x][y] == 1:
            for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                if 0 <= x + dx < 100 and 0 <= y + dy < 100:
                    if board[x + dx][y + dy] == 0:
                        cnt += 1

print(cnt)
