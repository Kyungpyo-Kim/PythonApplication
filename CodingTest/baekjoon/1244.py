"""

1. idea

단순 조건에 맞는 구현
switch 는 list 에 넣기
남 1 -> 배수 switch
여 2 -> 대칭 switch

N < 100
switches 
M < 100
students

2. complexity

time: N * M

3. data structure

switches: list

"""

import sys

input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))
M = int(input())
students = []
for _ in range(M):
    students.append(list(map(int, input().split())))

for s, n in students:
    if s == 1:
        for i in range(N):
            if (i + 1) % n == 0:
                switches[i] ^= 1
    if s == 2:
        switches[n - 1] ^= 1
        left = n - 2
        right = n
        while left >= 0 and right < N:
            if switches[left] == switches[right]:
                switches[left] ^= 1
                switches[right] ^= 1
                left -= 1
                right += 1
            else:
                break

for i in range(N):
    end = " "
    if i == N - 1:
        end = "\n"
    if (i + 1) % 20 == 0:
        end = "\n"

    print(switches[i], end=end)
