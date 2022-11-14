# 프로그래머스 레벨3 디스크컨트롤러 힙

import heapq

def solution(jobs):
    jobs.sort(key=lambda x: -x[0])
    num = len(jobs)
    start = 0
    end = 0
    time = 0
    
    q = []
    while jobs or q:
        while jobs and start <= jobs[-1][0] <= end:
            job = jobs.pop()
            heapq.heappush(q, (job[1], job[0]))
        if q:
            duration, init = heapq.heappop(q)
            start = end
            end += duration
            time += end - init
        else:
            end += 1

    return time // num


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]	
    print(solution(jobs))
    jobs = [[0, 6], [1, 2]]
    print(solution(jobs))
    