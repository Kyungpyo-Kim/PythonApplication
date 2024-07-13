"""

1. idea
- N
- backtracking 으로 완전 탐색 -> 메모리 초과
- greedy? implementation?

2. complexity
- time: N

3. data structure
4. category
- greedy or implementation?


"""

import sys

input = sys.stdin.readline

N = int(input())
counts = map(int, input().split())
order = [0] * N

for i, cnt in enumerate(counts):
    pos = -1
    while cnt >= 0:
        pos += 1
        if order[pos] == 0:
            cnt -= 1

    order[pos] = i + 1

print(*order)
