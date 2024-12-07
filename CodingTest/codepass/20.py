"""

- rotate 0, 120, 240
- flip

4가지 중 최솟값 찾기

0
1 0
1 0 0
0
0 0
0 0 1

0, 0 -> N-1, N-1
1, 0 -> N-1 - 1, N-1 - 1
2, 0 -> N-1 - 2, N-1 - 2

1
2 3
3 4 5
6 7 8 9
1 2 3 4 5

120 도 반시계로 돌리면 쉬워보임

x, y -> N-1 - y, x

5, 4, 3, 2, 1


"""

import copy
import sys

input = sys.stdin.readline

N = int(input())

tri_a = []
tri_b = []

for _ in range(N):
    tri_a.append(list(map(int, input().strip().split())))
for _ in range(N):
    tri_b.append(list(map(int, input().strip().split())))


def rotate(tri):
    new_tri = copy.deepcopy(tri)
    for i in range(N):
        for j in range(i + 1):
            new_tri[i][i - j] = tri[N - 1 - j][N - 1 - i]
    return new_tri


def flip(tri):
    for t in tri:
        t.reverse()
    return tri


def match(tri_a, tri_b):
    cnt = 0
    for i in range(N):
        for j in range(i + 1):
            if tri_a[i][j] != tri_b[i][j]:
                cnt += 1
    return cnt


answer = N * (N + 1) / 2


for i in range(3):
    for j in range(2):
        tri = copy.deepcopy(tri_a)
        for _ in range(i):
            tri = rotate(tri)
        for _ in range(j):
            tri = flip(tri)

        answer = min(answer, match(tri, tri_b))

print(answer)


def print_tri(tri):
    for i in range(N):
        print(*tri[i])


print_tri(tri_a)
tri = tri_a
for i in range(3):
    print("test: ", i)
    tri = rotate(tri)
    print_tri(tri)
