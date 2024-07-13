"""

1. idea
- 1, 0 count 하고
- 1은 앞에서 부터 지우고
- 0은 뒤에서 부터 지우면 끝

2. complexity
- time: 500

3. data structure
- map

4. category
- 문자열, 그리디

"""

# import sys

# input = sys.stdin.readline

# S = input().strip()

# cnt0 = S.count("0") // 2
# cnt1 = S.count("1") // 2

# S = list(S)

# i = len(S) - 1
# while cnt0 and (0 <= i < len(S)):
#     if S[i] == "0":
#         del S[i]
#         cnt0 -= 1
#     i -= 1

# i = 0
# while cnt1 and (0 <= i < len(S)):
#     if S[i] == "1":
#         del S[i]
#         cnt1 -= 1
#         i -= 1
#     i += 1

# print("".join(S))

import sys

input = sys.stdin.readline

S = list(input().strip())

cnt0 = S.count("0") // 2
cnt1 = S.count("1") // 2

for _ in range(cnt0):
    S.pop(-1 - S[::-1].index("0"))

for _ in range(cnt1):
    S.pop(S.index("1"))

print("".join(S))
