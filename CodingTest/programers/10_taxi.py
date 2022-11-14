from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):

    tree = defaultdict(list)
    for c, d, f in fares:
        tree[c].append((d, f))
        tree[d].append((c, f))

    max_fare = n**2 * 100000
    fare_map = [[max_fare for _ in range(n+1)] for _ in range(n+1)]
    for start in range(1, n+1):
        q = [(0, start)]
        while q:
            fare, node = heapq.heappop(q)
            if fare_map[start][node] < fare:
                continue
            fare_map[start][node] = fare

            for next_node, next_fare in tree[node]:
                if fare_map[start][next_node] > fare + next_fare:
                    heapq.heappush(q, (fare + next_fare, next_node))
    
    answer = max_fare
    for i in range(1, n+1):
        answer = min(answer, fare_map[s][i] + fare_map[i][a] + fare_map[i][b])
    return answer


if __name__ == "__main__":
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))

    n = 7
    s = 3
    a = 4
    b = 1
    fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    print(solution(n, s, a, b, fares))

    n = 6
    s = 4
    a = 5
    b = 6
    fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
    print(solution(n, s, a, b, fares))
