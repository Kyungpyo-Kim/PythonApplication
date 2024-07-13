"""

1. idea
왼쪽 R 로 옮기기
오른쪽 R로 옮기기
왼쪽 B로 옮기기
오른쪽 B 로 옮기기 -> 최솟값

2. complexity

3. data structure

4. category
- greedy


"""

import sys

input = sys.stdin.readline

N = int(input())
s = list(input().strip())

moves = []

i = 0
move = 0
while i < N:
    if s[i] == "R":
        i += 1
    else:
        break
while i < N:
    if s[i] == "R":
        move += 1
    i += 1
moves.append(move)

i = 0
move = 0
while i < N:
    if s[i] == "B":
        i += 1
    else:
        break
while i < N:
    if s[i] == "B":
        move += 1
    i += 1
moves.append(move)

i = N - 1
move = 0
while i >= 0:
    if s[i] == "R":
        i -= 1
    else:
        break
while i >= 0:
    if s[i] == "R":
        move += 1
    i -= 1
moves.append(move)

i = N - 1
move = 0
while i >= 0:
    if s[i] == "B":
        i -= 1
    else:
        break
while i >= 0:
    if s[i] == "B":
        move += 1
    i -= 1
moves.append(move)

print(min(moves))
