# 프로그래머스 레벨3 이중우선순위큐 힙

import heapq

def solution(operations):
    q = []
    for operation in operations:
        if "I" in operation:
            heapq.heappush(q, int(operation[2:]))
        if "D 1" in operation and q:
            q.pop(q.index(heapq.nlargest(1, q)[0]))
        if "D -1" in operation and q:
            heapq.heappop(q)
    
    if q:
        return [heapq.nlargest(1, q)[0], heapq.nsmallest(1, q)[0]]
    return [0, 0]


if __name__ == "__main__":
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    print(solution(operations))

    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))