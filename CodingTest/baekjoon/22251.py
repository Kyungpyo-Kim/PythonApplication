"""

1. idea
- N, K, P, X
- from 1 to N
- K digits
- change maximum P led
- find available changes from X
- find possible digit for each digit
- from 1 to N, count possible cases based on P

2. complexity
- 1 <= K <= 6 -> 10**6

3. data structure
4. category

"""

import sys

input = sys.stdin.readline


display = [
    [1, 1, 1, 0, 1, 1, 1],  # 0
    [0, 0, 1, 0, 0, 1, 0],  # 1
    [1, 0, 1, 1, 1, 0, 1],  # 2
    [1, 0, 1, 1, 0, 1, 1],  # 3
    [0, 1, 1, 1, 0, 1, 0],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 0, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
]

table = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        cnt = 0
        for a, b in zip(display[i], display[j]):
            if a != b:
                cnt += 1
        table[i][j] = cnt

N, K, P, X = map(int, input().split())

x = [0] * K
X = list(str(X))
for i in range(len(X)):
    x[-1 - i] = int(X[-1 - i])

ans = 0

for i in range(1, N + 1):
    y = [0] * K
    y_list = list(str(i))
    for j in range(len(y_list)):
        y[-1 - j] = int(y_list[-1 - j])

    cnt = 0
    for a, b in zip(x, y):
        cnt += table[a][b]

    # print(x, y, cnt)
    if cnt <= P:
        ans += 1

print(ans - 1)
