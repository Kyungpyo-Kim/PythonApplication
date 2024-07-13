"""

1. idea

N, 태수, P
랭킹 리스트

sort

태수의 점수가 업데이트 가능한지 확인
태수 포함 등수가 P 안에 드는지 체크

태수 점수의 등수 확인

2. complexity

time: sort NlogN + N + N
space: N

3. data structure
- score list
- rank map

"""

import sys

input = sys.stdin.readline

N, t_score, P = map(int, input().split())

scores = sorted(map(int, input().split()), reverse=True)

t_score_order = 1
for i in range(N):
    if scores[i] >= t_score:
        t_score_order += 1

rank = -1
if t_score_order <= P:
    scores.append(t_score)
    scores = sorted(scores, reverse=True)

    ranks = {}
    cur_rank = 1
    for i in range(N + 1):
        if i > 0 and scores[i] != scores[i - 1]:
            cur_rank = i + 1
        ranks[scores[i]] = cur_rank
    rank = ranks[t_score]

print(rank)
