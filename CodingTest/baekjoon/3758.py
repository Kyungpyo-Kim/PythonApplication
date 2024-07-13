"""

1. idea

- K
- id, pn, score

- T
- n, k, t, m
- m logs i, j, s

- map 으로 점수 리스트, 제출시간 저장
- [-최종점수, 제출한 횟수, 제출 시간] 으로 저장하고 sort

2. complexity

- map building time: m
- sort: n

3. data structure

- map, list

4. category

- implementation
- map
- sort

"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    n, k, t, m = map(int, input().split())

    scores = {}
    for log in range(m):
        i, j, s = map(int, input().split())

        if i not in scores:
            scores[i] = [[0 for _ in range(k + 1)], 0, m]

        scores[i][0][j] = max(scores[i][0][j], s)
        scores[i][1] += 1
        scores[i][2] = log

    scores_list = []
    for k, v in scores.items():
        scores_list.append([-sum(v[0]), v[1], v[2], k])

    scores_list = sorted(scores_list)

    rank = 0
    for i in range(len(scores_list)):
        if scores_list[i][-1] == t:
            rank = i + 1
            break

    print(rank)
