"""

1. idea
- 짧은 문자열 구하기 -> two pointer -> 시간 초과...
- dict 로 문자열 인덱스를 리스트로 저장하고 길이를 계산해서 min/max 구하기
- 투포인터로 모두 탐색하는게 느리다...

2. complexity

3. data structure
- list
- dict

4. category
- sliding window -> 시간 초과

"""

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())

    d = defaultdict(list)
    for i in range(len(W)):
        d[W[i]].append(i)

    longest = 0
    shortest = len(W) + 1
    for k, v in d.items():
        if len(v) >= K:
            for i in range(len(v) - K + 1):
                dist = v[i + K - 1] - v[i] + 1
                longest = max(dist, longest)
                shortest = min(dist, shortest)

    if longest != 0:
        print(shortest, longest)
    else:
        print(-1)
