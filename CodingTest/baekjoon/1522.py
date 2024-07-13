"""

1. idea
- 슬라이딩 윈도우 억지로 끌어들이면 풀 수 있는 방법이 생각남
- a 갯수만큼 연속으로 만들어야 함 -> a 갯수 ca
- ca 윈도우에 최소 b 의 갯수가 필요한 교환 횟수
- 원형 길이 처리를 위해 s + s 로 계산

2. complexity
- time N

3. data structure
- list

4. category
- 슬라이딩 윈도우

"""

import sys

input = sys.stdin.readline

s = list(input().strip())
n = len(s)
ca = s.count("a")

s = s + s

cb = s[:ca].count("b")
for i in range(1, n):
    cb = min(s[i : i + ca].count("b"), cb)

print(cb)
