"""
겹치는 영역을 어떻게 처리하나
하나, 두개만 겹칠 수 있고
여러개 동시에 겹칠 수 있음

소수점이 없으니
100x100 크기 board 만들고
색종이에 겹치는 부분 빼기

"""

import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().strip().split())) for _ in range(N)]

board = [[0] * 100 for _ in range(100)]

for a in arr:
    x, y = a
    for i in range(10):
        for j in range(10):
            board[x + i][y + j] = 1

print(sum([sum(b) for b in board]))
