"""

1. idea
- S 를 T 로 만들기
- S 뒤에 A 를 추가
- S 뒤에 B 를 추가하고 뒤집기
- len(S) < len(T)
- brute force: 2**(len(T) - len(S)) ~ 2**50 ~ 10**15 불가
- T 에서 S 로 만들면 경우의 수가 줄어들게 됨
- 재귀적으로 구현하면 함수가 쉽게 구현됨

2. complexity
3. data structure
4. category


"""

import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()


def solve(t):
    if len(t) == len(S):
        if t == S:
            return 1
        else:
            return 0

    ans = []
    if t[-1] == "A":
        ans.append(solve(t[:-1]))
    if t[0] == "B":
        ans.append(solve(t[1:][::-1]))
    if 1 in ans:
        return 1
    else:
        return 0


print(solve(T))
