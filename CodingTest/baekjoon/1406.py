"""

1. idea
- N: 100,000
- M: 500,000
- len(s) <= N <= 600,000
- 0 <= cur_pos <= len(s)
- priority queue 사용하면? -> stack 으로 더 빠르게 구현
  - (index, value) 형태로 저장
  - left, right pq 를 두개 생성
  - left, right 에 따라서 두개 queue 를 빼고 더함

2. complexity
- time: M

3. data structure
- stack

4. category
- simulation
- stack

"""

import sys

input = sys.stdin.readline

s = input().strip()

left = []
right = []

for i, v in enumerate(s):
    left.append(v)

M = int(input())

for _ in range(M):
    cmd = input()
    if cmd.startswith("L"):
        if left:
            right.append(left.pop())
    elif cmd.startswith("D"):
        if right:
            left.append(right.pop())
    elif cmd.startswith("B"):
        if left:
            left.pop()
    elif cmd.startswith("P"):
        elem = cmd.split()[-1]
        left.append(elem)
    else:
        raise RuntimeError

ans = left + right[::-1]
print("".join(ans))
