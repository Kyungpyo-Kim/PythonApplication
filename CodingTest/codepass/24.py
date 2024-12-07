"""

A
B
A + B
A + B + B
A + B + A + B + B
A + B + A + B + B + A + B + B
...

N 일 동안 A, B 가 몇개인지
그리고 x*A + y*B 를 만족하는 A, B 찾기

"""

import sys

input = sys.stdin.readline

D, K = map(int, input().strip().split())

cnt_a, cnt_b = 0, 0
pre1_a, pre1_b = 0, 1
pre2_a, pre2_b = 1, 0

for i in range(D - 2):
    cnt_a = pre1_a + pre2_a
    cnt_b = pre1_b + pre2_b
    pre2_a, pre2_b = pre1_a, pre1_b
    pre1_a, pre1_b = cnt_a, cnt_b

b, A, B = 1, 0, 0
while A == B == 0:

    for i in range(b):
        a = i + 1
        if K == cnt_a * a + cnt_b * b:
            A, B = a, b
            break
    b += 1

print(A)
print(B)
