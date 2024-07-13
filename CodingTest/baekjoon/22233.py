"""

1. idea
- N, M
- keywords
- used keywords
- using set, save keywords
- remove used keywords from set and print length of keywords set

2. complexity
- N + M

3. data structure
- set

4. category
- set

"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

k = set()

for _ in range(N):
    k.add(input().strip())

for _ in range(M):
    used_k = set(input().strip().split(","))
    k = k - used_k
    print(len(k))
