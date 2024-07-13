"""

1. idea

dict 로 단어수 count
단어수, 길이, 단어 로 tuple 만들어서 sort

2. complexity

time: NlogN for sort

3. data structure

- dict for word freq count
- list for sort

"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

freq = {}
for _ in range(N):
    w = input().strip()
    if len(w) >= M:
        if w not in freq:
            freq[w] = 0
        else:
            freq[w] += 1

words = []
for k, v in freq.items():
    words.append((-v, -len(k), k))

words = sorted(words)
for w in words:
    print(w[-1])
