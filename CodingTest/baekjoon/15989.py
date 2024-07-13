"""

1. idea
- dp
- 순서가 다른 것은 같은 걸로 친다...
- 모두 1로 더하는 경우 dp = [1] * 10001
- 2로 더하는 경우 dp[n] += dp[n-2]
- 3로 더하는 경우 dp[n] += dp[n-3]

2. complexity
- time N

3. data structure
- list

4. category
- DP


"""

import sys

input = sys.stdin.readline

dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]

T = int(input())
for _ in range(T):
    print(dp[int(input())])
