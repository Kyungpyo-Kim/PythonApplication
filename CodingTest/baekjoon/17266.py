"""

1. idea

N
M
x

간격 중 가장 긴 길이 찾기
x for 돌면서 간격 저장, max 찾기
이때, 처음 왼쪽, 마지막 오른쪽 빼고는 간격 절반만 필요 

2. complexity

max 찾는 sort MlogM

3. data structure

list for intervals


"""

import sys

input = sys.stdin.readline


N = int(input())
M = int(input())
x = list(map(int, input().split()))

intervals = [x[0], N - x[-1]]

x.append(N)
for i in range(M - 1):
    intervals.append((x[i + 1] - x[i] + 1) // 2)

print(max(intervals))
