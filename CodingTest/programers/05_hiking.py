# 프로그래머스 레벨3 등산코스 정하기 2022카카오테크인턴쉽
import heapq
from collections import defaultdict
graph = defaultdict(list)
huge_val = 1000000007
intensities = [huge_val for _ in range(50001)]

def daikstra(n, start, summits):
    visited = set()

    pq = []
    intensities[start] = 0
    heapq.heappush(pq, (intensities[start], start))

    while pq:
        intensity, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        for next_intensity, next_node in graph[node]:
            tmp = max(intensity, next_intensity)
            if tmp < intensities[next_node]:
                intensities[next_node] = tmp
                if next_node not in summits:
                    heapq.heappush(pq, (tmp, next_node))
                    
def solution(n, paths, gates, summits):
    for i, j, w in paths:
        graph[i].append([w, j])
        graph[j].append([w, i])

    summits = set(summits)

    for gate in gates:
        daikstra(n, gate, summits)

    min_intensity = huge_val
    min_summit = 0
    for summit in summits:
        if intensities[summit] == min_intensity:
            min_summit = min(min_summit, summit)
        if intensities[summit] < min_intensity:
            min_intensity = intensities[summit]
            min_summit = summit
    return [min_summit, min_intensity]

if __name__ == "__main__":
    # n = 6
    # paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
    # gates = [1, 3]	
    # summits = [5]
    # print(solution(n, paths, gates, summits))
    # n = 7
    # paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]	
    # gates = [1]	
    # summits = [2, 3, 4]	
    # print(solution(n, paths, gates, summits))
    # n = 7
    # paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]	
    # gates = [3, 7]	
    # summits = [1, 5]
    # print(solution(n, paths, gates, summits))
    n = 5
    paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]	
    gates = [1, 2]	
    summits = [5]
    print(solution(n, paths, gates, summits))
