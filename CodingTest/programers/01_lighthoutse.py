# 프로그래머스 레벨 3 - 등대 - 연습문제

import sys

sys.setrecursionlimit(1000000)

def dfs(node, tree, visited):
    visited[node] = True
    children = [child for child in tree[node] if not visited[child]]
    pick, not_pick = 1, 0
    
    if not children:
        return pick, not_pick

    for child in children:
        child_pick, child_not_pick = dfs(child, tree, visited)
        pick += min(child_pick, child_not_pick)
        not_pick += child_pick
    return pick, not_pick


def solution(n, lighthouse):

    # make tree from lighthouse
    tree = [[] for _ in range(n+1)]
    for a, b in lighthouse:
        tree[a].append(b)
        tree[b].append(a)

    visited = [False for _ in range(n+1)]
    root = 1

    return min(dfs(root, tree, visited))

if __name__ == "__main__":
    n = 8
    lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]
    print(solution(n, lighthouse))

    n = 10
    lighthouse = [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]
    print(solution(n, lighthouse))

