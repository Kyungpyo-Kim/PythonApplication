"""

1. idea
- N 이 500 -> N**2 까지 가능
- index 기준으로 왼쪽 max, 오른쪽 max 를 구하고, min 값이 빗물 고이는 기준

2. complexity
- time: N**2
 
3. data structure
- list

4. category
- 단순 구현?

"""

import sys

input = sys.stdin.readline

H, W = map(int, input().split())

arr = list(map(int, input().split()))

rain = 0
for i in range(1, W - 1):
    left_max = max(arr[:i])
    right_max = max(arr[i + 1 :])
    height = min(left_max, right_max)
    if height > arr[i]:
        rain += height - arr[i]

print(rain)
