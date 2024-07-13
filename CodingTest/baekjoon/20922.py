"""

1. idea
- N, K
- 슬라이딩 윈도우

2. complexity
- time: N

3. data structure
- list

4. category
- 슬라이딩 윈도우 / 투 포인터

"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
seq = list(map(int, input().split()))

count = {}
left = 0
max_length = 0
for right in range(N):
    if seq[right] not in count:
        count[seq[right]] = 0

    count[seq[right]] += 1

    while count[seq[right]] > K:
        count[seq[left]] -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
