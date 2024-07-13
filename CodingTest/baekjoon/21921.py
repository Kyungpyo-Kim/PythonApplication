"""

1. idea

N, X
visits

for 돌면서 max count

2. complexity

time: N + X

3. data structure

None

"""

import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visits = list(map(int, input().split()))

val = sum(visits[:X])
max_val = val
max_cnt = 1
for i in range(1, N - X + 1):
    val = val + visits[i + X - 1] - visits[i - 1]
    if max_val < val:
        max_val = val
        max_cnt = 1
    elif max_val == val:
        max_cnt += 1

if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(max_cnt)
