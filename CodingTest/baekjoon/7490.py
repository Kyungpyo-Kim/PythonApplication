"""

1. idea
- brute force
- 3 <= N <= 9 -> 3**9
- implement recursively like permutation calculation

2. complexity
- 3**9

3. data structure
- list

4. category
- 구현
- 문자열
- 브루트포스 알고리즘
- 백트래킹

"""

import sys

input = sys.stdin.readline

T = int(input())


def calculate(ans):
    ans = "".join(ans[::-1])
    ans = ans.replace(" ", "")
    return eval(ans)


def make_zero(n, ans, result):
    if n == 1:
        ans += ["1"]
        if calculate(ans) == 0:
            result.append("".join(ans[::-1]))
        return

    ans += [str(n)]
    for op in ["+", "-", " "]:
        tmp = ans + [op]
        make_zero(n - 1, tmp, result)


for _ in range(T):
    N = int(input())
    result = []
    make_zero(N, [], result)

    result = sorted(result)

    print("\n".join(result))
    print()
