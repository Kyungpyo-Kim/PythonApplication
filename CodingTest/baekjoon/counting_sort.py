import sys
input = sys.stdin.readline

n = int(input())
cnt = [0 for _ in range(10001)]

for _ in range(n):
    cnt[int(input())] += 1

for i, c in enumerate(cnt):
    if c:
        for _ in range(c):
            print(i)