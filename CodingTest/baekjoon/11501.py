"""

1. idea
- buy
- sell
- do nothing
- 주가가 떨어지기 전 max 로 판다고 가정

2. complexity
- time: N

3. data structure
- list

4. category
- greedy

"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    days = int(input())
    prices = list(map(int, input().split()))

    i = len(prices) - 2
    price = prices[-1]
    profit = 0
    while i >= 0:
        if price > prices[i]:
            profit += price - prices[i]
        else:
            price = prices[i]
        i -= 1
    print(profit)
