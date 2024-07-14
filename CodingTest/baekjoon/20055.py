"""

1. idea
- N, K
- simulation
- deque 이용해서 rotation 해서 계산에 적용

2. complexity
- time: N * K * max(A)
3. data structure
- list

4. category
- simulation
- implementation
- deque

"""

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

arr = deque(map(int, input().split()))
robots = deque([0] * N)

count = 0
step = 0

while count < K:
    step += 1
    arr.rotate(1)
    robots.rotate(1)
    robots[0] = 0
    robots[-1] = 0

    for i in range(N - 1, 0, -1):
        if arr[i] > 0 and robots[i - 1] == 1 and robots[i] == 0:
            robots[i - 1] = 0
            robots[i] = 1
            arr[i] -= 1
            if arr[i] == 0:
                count += 1

    if arr[0] > 0:
        arr[0] -= 1
        robots[0] = 1
        if arr[0] == 0:
            count += 1

print(step)
