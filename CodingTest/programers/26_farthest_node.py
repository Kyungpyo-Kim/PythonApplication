# 프로그래머스 레벨3 가장먼노드 그래프
import heapq
from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    max_val = 50001
    dist_map = [max_val for _ in range(n+1)]
    visited = set()
    pq = []
    heapq.heappush(pq, [0, 1])
    dist_map[1] = 0
    visited.add(1)
    while pq:
        dist, node = heapq.heappop(pq)
        children = [child for child in graph[node] if child not in visited]
        for child in children:
            if dist_map[child] > dist + 1:
                dist_map[child] = dist + 1
                heapq.heappush(pq, [dist_map[child], child])

    answer = 0
    max_dist = max(dist_map[1:])
    for i in dist_map[1:]:
        if i == max_dist:
            answer += 1
    return answer

if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))