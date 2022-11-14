# 프로그래머스 레벨3 - 부대복귀 - 연습문제

from collections import defaultdict,deque

def solution(n, roads, sources, destination):
    tree = defaultdict(list)

    for a, b in roads:
        tree[a].append(b)
        tree[b].append(a)

    visited = set()
    distance_map = [-1 for _ in range(n+1)]

    queue = deque([destination])
    visited.add(destination)
    distance_map[destination] = 0
    while queue:
        node = queue.popleft()
        children = [child for child in tree[node] if child not in visited]
        for child in children:
            visited.add(child)
            distance_map[child] = distance_map[node] + 1
            queue.append(child)

    return [distance_map[source] for source in sources]


if __name__ == "__main__":
    n = 3
    roads = [[1, 2], [2, 3]]	
    sources = [2, 3]
    destination = 1
    print(solution(n, roads, sources, destination))

    n = 5
    roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]	
    sources = [1, 3, 5]	
    destination = 5	
    print(solution(n, roads, sources, destination))
