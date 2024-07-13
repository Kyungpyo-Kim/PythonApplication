"""

1. idea

T
N
data

- data 를 가지고 6명 되는 팀만 골라냄
- 팀원들에 점수 먹이기
- 팀 점수, 5등 점수 저장
- 점수 비교 + 5등 점수 비교

2. complexity

time: N
space: N

3. data structure

6명팀 골라내기 dict[팀] = 명수
팀별 점수 dict[팀] = [총 점수, 5등 점수]

"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    finish = {}

    for d in data:
        if d not in finish:
            finish[d] = 1
        else:
            finish[d] += 1

    candi = []
    for k, v in finish.items():
        if v >= 6:
            candi.append(k)

    scores = {}
    score = 1
    for d in data:
        if d in candi:
            if d not in scores:
                scores[d] = []
            scores[d].append(score)
            score += 1

    winner = None
    for k, v in scores.items():
        if winner is None:
            winner = [k, sum(v[:4]), v[4]]
            continue

        cur = [k, sum(v[:4]), v[4]]
        if cur[1] < winner[1]:
            winner = cur
            continue

        elif cur[1] == winner[1]:
            if cur[2] < winner[2]:
                winner = cur

    print(winner[0])
