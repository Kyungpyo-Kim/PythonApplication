# 프로그래머스 레벨3 순위 그래프
from collections import defaultdict

def solution(n, results):
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    for result in results:
        win_graph[result[0]].append(result[1])
        lose_graph[result[1]].append(result[0])

    win_table = [0 for _ in range(n+1)]
    lose_table = [0 for _ in range(n+1)]

    for graph, table in zip([win_graph, lose_graph], [win_table, lose_table]):
        for i in range(1, n+1):
            visited = set()
            stack = [i]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(graph[node])
            table[i] = len(visited)

    answer = 0
    for i in range(1, n+1):
        if win_table[i] + lose_table[i] == n + 1:
            answer += 1
    return answer

"""
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer
"""


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))