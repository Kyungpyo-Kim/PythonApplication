from collections import defaultdict, deque
from typing import List


def tuple2str(t):
    return "".join(map(str, t))


class Solver:
    def __init__(self, N: int, mMap: List[List[int]]):
        self.N = N
        self.mm = [[0] * (N + 2) for _ in range(N + 2)]
        for r in range(N):
            for c in range(N):
                self.mm[r + 1][c + 1] = mMap[r][c]

        self.c_cnt = defaultdict(int)
        self.c_list = defaultdict(list)

        self.c_cnt[tuple2str([0])] += N * N
        for r in range(N):
            for c in range(N):
                self.c_list[tuple2str([0])].append([(r, c)])

        for l in range(2, 6):
            for r in range(N):
                for c in range(N):
                    if c + l < N + 1:
                        tmp = mMap[r][c : c + l]
                        tmp_list = [(r, c + i) for i in range(l)]

                        tmp_max = max(tmp)
                        tmp = [tmp_max - t for t in tmp]
                        self.c_cnt[tuple2str(tmp)] += 1
                        self.c_list[tuple2str(tmp)].append(tmp_list)

                        if tmp != tmp[::-1]:
                            self.c_cnt[tuple2str(tmp[::-1])] += 1
                            self.c_list[tuple2str(tmp[::-1])].append(tmp_list[::-1])

                    if r + l < N + 1:
                        tmp = [mMap[r + i][c] for i in range(l)]
                        tmp_list = [(r + i, c) for i in range(l)]

                        tmp_max = max(tmp)
                        tmp = [tmp_max - t for t in tmp]
                        self.c_cnt[tuple2str(tmp)] += 1
                        self.c_list[tuple2str(tmp)].append(tmp_list)

                        if tmp != tmp[::-1]:
                            self.c_cnt[tuple2str(tmp[::-1])] += 1
                            self.c_list[tuple2str(tmp[::-1])].append(tmp_list[::-1])

    def numberOfCandidate(self, M: int, mStructure: List[int]) -> int:
        ms = mStructure[:M]
        ms_min = min(ms)
        ms = tuple2str(m - ms_min for m in ms)
        return self.c_cnt[ms]

    def maxArea(self, M: int, mStructure: List[int], mSeaLevel: int) -> int:
        ms = mStructure[:M]
        ms_min = min(ms)
        ms = tuple2str(m - ms_min for m in ms)
        if self.c_cnt[ms] == 0:
            return -1

        ans = 0
        for cl in self.c_list[ms]:
            for i in range(M):
                r, c = cl[i]
                self.mm[r + 1][c + 1] += mStructure[i]

            ans = max(ans, self.bfs(self.N, self.mm, mSeaLevel))

            for i in range(M):
                r, c = cl[i]
                self.mm[r + 1][c + 1] -= mStructure[i]

        return ans

    @staticmethod
    def bfs(N, mm, mSeaLevel):
        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))
        cnt = (N + 2) ** 2

        while q:
            r, c = q.popleft()
            cnt -= 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                if 0 <= nr < N + 2 and 0 <= nc < N + 2 and mm[nr][nc] < mSeaLevel:
                    visited.add((nr, nc))
                    q.append((nr, nc))

        return cnt


global solver


def init(N: int, mMap: List[List[int]]) -> None:
    global solver
    solver = Solver(N, mMap)
    return


def numberOfCandidate(M: int, mStructure: List[int]) -> int:
    global solver
    return solver.numberOfCandidate(M, mStructure)


def maxArea(M: int, mStructure: List[int], mSeaLevel: int) -> int:
    global solver
    return solver.maxArea(M, mStructure, mSeaLevel)


import sys

# from solution import init, maxArea, numberOfCandidate

CMD_INIT = 1
CMD_NUMBER_OF_CANDIDATE = 2
CMD_MAX_AREA = 3


def run():
    numQuery = int(sys.stdin.readline())
    isCorrect = False
    mMap = [[0 for _ in range(20)] for __ in range(20)]
    mStructure = [0 for _ in range(5)]

    for q in range(numQuery):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            for i in range(N):
                for j in range(N):
                    mMap[i][j] = int(next(inputs))
            init(N, mMap)
            isCorrect = True

        elif cmd == CMD_NUMBER_OF_CANDIDATE:
            M = int(next(inputs))
            for i in range(M):
                mStructure[i] = int(next(inputs))
            userAns = numberOfCandidate(M, mStructure)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False
                print("fail!!!!!!")

        elif cmd == CMD_MAX_AREA:
            M = int(next(inputs))
            for i in range(M):
                mStructure[i] = int(next(inputs))
            mSeaLevel = int(next(inputs))
            userAns = maxArea(M, mStructure, mSeaLevel)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

    return isCorrect


import cProfile
import pstats

if __name__ == "__main__":
    # sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    profiler = cProfile.Profile()
    profiler.enable()

    # TC = 1
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)

    profiler.disable()
    stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
