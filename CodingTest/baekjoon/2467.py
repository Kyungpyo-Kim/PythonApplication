"""

1. idea
- N: 100,000 -> brute force: N**2, 시간초과
- 가장 큰거, 가장 작은거 부터 시작해서 0에 근사하도록 투포인터를 옮기기
- 최소값을 계속 저장하고, 모두 탐색할때까지 서치

2. complexity
- 탐색 N

3. data structure
- list

4. category
- 투포인터

"""

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1

ans = (arr[left], arr[right])
val_min = abs(arr[left] + arr[right])
while left < right:
    val = arr[left] + arr[right]

    if val_min > abs(val):
        val_min = abs(val)
        ans = (arr[left], arr[right])

    if val > 0:
        right -= 1
    else:
        left += 1

print(*ans)
