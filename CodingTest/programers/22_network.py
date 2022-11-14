# 프로그래머스 레벨3 네트워크 깊이너비우선탐색

from collections import deque


def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i in visited:
            continue

        visited.add(i)
        q = deque([i])
        while q:
            c = q.popleft()
            child = [
                j
                for j in range(n)
                if computers[c][j] == 1 and c != j and j not in visited
            ]
            for c in child:
                visited.add(c)
                q.append(c)

        answer += 1
    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))

    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))
