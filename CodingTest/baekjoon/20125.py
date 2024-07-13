"""
1. idea

find head -> 팔 위치, 허리 위치
팔길이 계산 left, right
허리 길이 계산 -> 다리 위치
다리 길이 계산 left, right

2. time complexity

graph building: N^2
cal: O(1)

3. data structure

graph

"""

import sys

input = sys.stdin.readline

N = int(input())

g = [["" for _ in range(N)] for _ in range(N)]

head = None
d = ((0, -1), (0, +1), (+1, 0))  # left, right, down

for i in range(N):
    row = input().strip()
    for j in range(N):
        g[i][j] = row[j]
        if head is None and g[i][j] == "*":
            head = (i, j)


def cal_length(pos, d):
    length = 1
    while True:
        pos[0] += d[0]
        pos[1] += d[1]

        if pos[0] >= N or pos[1] >= N:
            break
        if pos[0] < 0 or pos[1] < 0:
            break

        if g[pos[0]][pos[1]] == "*":
            length += 1
        else:
            break

    return length, pos


pos = [head[0] + 1, head[1] - 1]
left_arm, _ = cal_length(pos, d[0])

pos = [head[0] + 1, head[1] + 1]
right_arm, _ = cal_length(pos, d[1])

pos = [head[0] + 2, head[1]]
waist, last = cal_length(pos, d[2])

pos = [last[0], last[1] - 1]
left_leg, _ = cal_length(pos, d[2])

pos = [last[0], last[1] + 1]
right_leg, _ = cal_length(pos, d[2])

print(head[0] + +2, head[1] + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
