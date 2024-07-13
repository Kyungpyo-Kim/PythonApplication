"""

1. idea

- backtracking 으로 recursive 하게 구현
- 최소 값으로 출력, 
- 전에 갔던 곳은 갈 수 없음
- 2  <= N, M <= 6

2. complexity

- recursion limit: 6^6

3. data structure

- dp map

4. category

- dp
- graph
- brute force

"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

dp = [[None for _ in range(M)] for _ in range(N)]
fuel_amp = [[None for _ in range(M)] for _ in range(N)]
for i in range(N):
    row = map(int, input().split())
    for j, v in enumerate(row):
        fuel_amp[i][j] = v


def get_min_fuel(i, j, prev):
    global fuel_amp

    if i == N - 1:
        return fuel_amp[i][j]

    fuel = []
    if prev != 1 and i + 1 < N and j - 1 >= 0:
        fuel.append(get_min_fuel(i + 1, j - 1, 1))
    if prev != 2 and i + 1 < N:
        fuel.append(get_min_fuel(i + 1, j, 2))
    if prev != 3 and i + 1 < N and j + 1 < M:
        fuel.append(get_min_fuel(i + 1, j + 1, 3))

    return min(fuel) + fuel_amp[i][j]


min_fuel = min(get_min_fuel(0, i, 0) for i in range(M))
print(min_fuel)
