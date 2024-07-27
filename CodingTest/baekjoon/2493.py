"""

1. idea
- N (500,000), arr
- brute force -> N**2
- two pointer 사용 x
- heapq 사용 x
- stack 사용
    - stack 에 수신 탑만 넣기


2. complexity
- N

3. data structure
- list
- stack

4. category
- stack

"""

import sys

input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
n = [0] * N

r = [(s[0], 1)]
for i in range(1, N):
    if r:
        while r:
            receiver, num = r.pop()
            if s[i] < receiver:
                n[i] = num
                r.append((receiver, num))
                break

    r.append((s[i], i + 1))

print(*n)
