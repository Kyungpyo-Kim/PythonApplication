"""

1. idea
- -k ~ N 까지 sliding 하면서 max 값 찾기

2. complexity
- N * k

3. data structure
- list

4. category
- 브루트포스 알고리즘
- 두 포인터
- 슬라이딩 윈도우

"""

import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [0] * N
for i in range(N):
    sushi[i] = int(input())

for i in range(k):
    sushi.append(sushi[i])

max_k = 0
for i in range(N):
    ks = set(sushi[i : i + k])
    ks.add(c)
    max_k = max(max_k, len(ks))

print(max_k)
