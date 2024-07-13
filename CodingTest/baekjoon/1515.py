"""

1. idea

1 ~ N 까지 돌면서 str 바꾸면서 하나씩 지우기
한 숫자에서 여러개 지워질 수 있음

2. time complexity

time: N

3. data structure

4. category

구현, 브루트포스

"""

import sys

input = sys.stdin.readline

N = input().strip()

n = 1
j = 0

while True:
    str_n = str(n)

    for s in str_n:
        if s == N[j]:
            j += 1
            if j == len(N):
                break

    if j == len(N):
        break
    n += 1

print(n)
