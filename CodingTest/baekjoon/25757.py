"""
1. idea
Y: 2, F: 3, O: 4
N

make set, len(set) / 2 or 3 or 4

2. complexity

time O(N) for building set

3. data structure

set


"""

import sys

input = sys.stdin.readline

gn = {"Y": 1, "F": 2, "O": 3}

N, game = input().split()
candidates = set()
for _ in range(int(N)):
    candidates.add(input().strip())

print(len(candidates) // gn[game])
