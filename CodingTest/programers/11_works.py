# 프로그래머스 레벨3 야근지수 연습문제


def solution(n, works):
    def workload(height):
        return sum([work - height for work in works if work > height])

    left = 0
    right = max(works)
    while left < right:
        mid = (left + right) // 2
        if workload(mid) <= n:
            right = mid
        else:
            left = mid + 1

    for i in range(len(works)):
        if works[i] > right:
            n -= works[i] - right
            works[i] = right
    
    works.sort(reverse=True)
    while n:
        if works[0] == 0:
            return 0
        works[0] -= 1
        n -= 1
        works.sort(reverse=True)
    
    return sum([work**2 for work in works])

"""
heapq를 이용한 풀이

import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
        
    q = []
    for work in works:
        heapq.heappush(q, -work)
    
    while n:
        if q[0] == 0:
            return 0
        heapq.heappush(q, heapq.heappop(q) + 1)
        n -= 1

    return sum([work**2 for work in q])
"""

if __name__ == "__main__":
    n = 4
    works = [4, 3, 3]
    print(solution(n, works))

    n = 1
    works = [2, 1, 2]
    print(solution(n, works))

    n = 3
    works = [1, 1]
    print(solution(n, works))
