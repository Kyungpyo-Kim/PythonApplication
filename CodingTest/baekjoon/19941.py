"""

1. idea

N, K
햄버거 리스트 만들고 먹었는지 체크
왼쪽부터 체크

2. complexity

time N * K

3. data structure

hbg = list

4. category
- greedy
- implementation

"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

hp = input().strip()
h = [0 for _ in range(N)]
p = [0 for _ in range(N)]

for i in range(N):
    if hp[i] == "H":
        h[i] = 1
    elif hp[i] == "P":
        p[i] = 1

p_cnt = 0
for i in range(N):
    if p[i] == 1:
        for j in range(i - K, i + K + 1):
            if j < 0 or j >= N:
                continue
            if h[j] == 1:
                h[j] = 0
                p_cnt += 1
                break

print(p_cnt)
