"""

1. idea
- DFS 로 완전 탐색 time: N! -> 시간 초과
- DFS 로 cycle 체크, 첫째줄과 둘째줄의 간선을 생성해서 cycle 이 생성되면 집합에 포함
   -> cycle 체크로 조건을 확인하는 아이디어가 중요
- 그래프를 생성할때 양방향이면 안됨

2. complexity
time: V = N, E = N, ~ NlogN

3. data structure
- graph
- set

4. category
- DFS

"""

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for i in range(N):
    elem = int(input())
    graph[i + 1].append(elem)


def is_cycle(i):
    visited = [0] * (N + 1)

    def dfs(cur, start):
        if visited[cur]:
            if cur == start:
                return True
            else:
                return False

        visited[cur] = 1
        for elem in graph[cur]:
            if dfs(elem, start):
                return True

        return False

    return dfs(i, i)


ans = []
for i in range(1, N + 1):
    if is_cycle(i):
        ans.append(i)

print(len(ans))
print("\n".join(map(str, ans)))
