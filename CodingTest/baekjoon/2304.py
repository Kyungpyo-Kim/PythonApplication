"""

1. idea
- max 값으로 시작 ~ max, max ~ max, max ~ end 구해서 각각 더하기

2. complexity
- time: NlogN for finding max values

3. data structure
- list

4. category
- brute force

"""

import sys

input = sys.stdin.readline

N = int(input())

heights = [0 for _ in range(1001)]

for _ in range(N):
    pos, height = map(int, input().split())
    heights[pos] = height

max_height = max(heights)

max_left = 0
while True:
    if heights[max_left] == max_height:
        break
    else:
        max_left += 1

max_right = 1000
while True:
    if heights[max_right] == max_height:
        break
    else:
        max_right -= 1

area = max_height * (max_right - max_left + 1)

height = 0
i = 0
while i < max_left:
    if heights[i] > height:
        height = heights[i]
    area += height
    i += 1

height = 0
i = 1000
while i > max_right:
    if heights[i] > height:
        height = heights[i]
    area += height
    i -= 1

print(area)
