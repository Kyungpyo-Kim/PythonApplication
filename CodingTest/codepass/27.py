"""

111 ~ 999 까지 만들고
조건에 따라 지우기
set 으로 만들어서 지우기

"""

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())

arr = [input().strip().split() for _ in range(N)]

cnt = 0
for p in permutations(range(1, 10), 3):

    is_answer = True
    for ar in arr:
        a, s, b = ar
        cnt_s, cnt_b = 0, 0
        for i in range(3):
            if p[i] == int(a[i]):
                cnt_s += 1
            for j in range(3):
                if i != j and p[i] == int(a[j]):
                    cnt_b += 1
        if int(s) != cnt_s or int(b) != cnt_b:
            is_answer = False
            break
    if is_answer:
        cnt += 1

print(cnt)
