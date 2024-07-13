"""

1. idea

- N
- 비슷한 단어 찾기
- first 를 list 로 만들기
- second 에 단어를 하나씩 remove 로 지우기
- 남은 first_list 가 1보다 작거나 같고, 다른 단어가 1보다 작거나 같을때 비슷한 단어

2. complexity

time: 10*10*N

3. data structure

set

4. category

구현, 문자열

"""

# import sys

# input = sys.stdin.readline

# N = int(input())

# first = input().strip()
# cnt = 0
# for _ in range(N - 1):
#     second = input().strip()

#     if len(first) - len(second) >= 2:
#         continue
#     if len(first) - len(second) <= -2:
#         continue

#     check_s = [0 for _ in range(len(second))]
#     c = 0
#     for f in first:
#         for j in range(len(second)):
#             if check_s[j]:
#                 continue

#             if f == second[j]:
#                 c += 1
#                 check_s[j] = 1
#                 break

#     if c == min(len(first), len(second)):
#         cnt += 1
#     elif c == len(first) - 1 and len(first) == len(second):
#         cnt += 1

# print(cnt)


import sys

input = sys.stdin.readline

N = int(input())

first = input().strip()

cnt = 0
for _ in range(N - 1):
    second = input().strip()
    target = list(first)

    diff = 0
    for s in second:
        if s in target:
            target.remove(s)
        else:
            diff += 1

    if len(target) <= 1 and diff <= 1:
        cnt += 1

print(cnt)
