import copy
import heapq
from typing import List

# from bisect import bisect_left, insort_left


class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance


class Solver:
    def __init__(self, N: int, M: int, L: int, mXs: List[int], mYs: List[int]) -> None:
        self.N = N
        self.M = M
        self.L = L
        self.taxis: List[Result] = []  # position, move/ride distance
        self.grid_size = self.N // self.L + 1
        self.grid = [[[] for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for i in range(self.M):
            self.taxis.append(Result(mXs[i], mYs[i], 0, 0))
            gx, gy = mXs[i] // self.L, mYs[i] // self.L
            self.grid[gx][gy].append(i)

        self.q = [(0, i + 1) for i in range(self.M)]
        heapq.heapify(self.q)

        self.update = set()

        # self.q = []
        # for i in range(self.M):
        #     insort_left(self.q, (0, i + 1))

    def pickup(self, mSX: int, mSY: int, mEX: int, mEY: int) -> int:
        gx, gy = mSX // self.L, mSY // self.L
        grid = self.grid
        taxis = self.taxis

        dist_move = self.L + 1
        tid = self.M
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= gx + dx < self.grid_size and 0 <= gy + dy < self.grid_size:
                    for i in grid[gx + dx][gy + dy]:
                        dist = abs(mSX - taxis[i].mX) + abs(mSY - taxis[i].mY)
                        if dist <= self.L and (dist, i) < (dist_move, tid):
                            tid, dist_move = i, dist

        if tid == self.M:
            return -1

        taxi = taxis[tid]
        gx, gy = taxi.mX // self.L, taxi.mY // self.L
        grid[gx][gy].remove(tid)
        gx, gy = mEX // self.L, mEY // self.L
        grid[gx][gy].append(tid)

        # cur_dist = taxis[tid].mRideDistance
        # idx = bisect_left(self.q, (-cur_dist, tid + 1))
        # del self.q[idx]

        dist_ride = abs(mSX - mEX) + abs(mSY - mEY)
        taxis[tid].mMoveDistance += dist_move + dist_ride
        taxis[tid].mRideDistance += dist_ride
        taxis[tid].mX = mEX
        taxis[tid].mY = mEY

        # heapq.heappush(self.q, (-taxis[tid].mRideDistance, tid + 1))
        # insort_left(self.q, ((-taxis[tid].mRideDistance, tid + 1)))

        self.update.add(tid)

        return tid + 1

    def reset(self, mNo: int) -> Result:
        taxis = self.taxis
        ret = copy.deepcopy(taxis[mNo - 1])

        # idx = bisect_left(self.q, (-ret.mRideDistance, mNo))
        # del self.q[idx]
        # insort_left(self.q, (0, mNo))

        taxis[mNo - 1].mMoveDistance = 0
        taxis[mNo - 1].mRideDistance = 0

        # heapq.heappush(self.q, (0, mNo))

        self.update.add(mNo - 1)

        return ret

    def getBest(self, mNos: List[int]) -> None:
        q = self.q
        taxis = self.taxis

        for i in self.update:
            heapq.heappush(q, (-taxis[i].mRideDistance, i + 1))
        self.update = set()

        cnt = 0
        ts = []
        while cnt < 5:
            t = heapq.heappop(q)
            if taxis[t[1] - 1].mRideDistance == -t[0] and t not in ts:
                mNos[cnt] = t[1]
                ts.append(t)
                cnt += 1

        for t in ts:
            heapq.heappush(q, t)

        # for i in range(5):
        #     mNos[i] = self.q[i][1]


global solver


def init(N: int, M: int, L: int, mXs: List[int], mYs: List[int]) -> None:
    global solver
    solver = Solver(N, M, L, mXs, mYs)


def pickup(mSX: int, mSY: int, mEX: int, mEY: int) -> int:
    global solver
    return solver.pickup(mSX, mSY, mEX, mEY)


def reset(mNo: int) -> Result:
    global solver
    return solver.reset(mNo)


def getBest(mNos: List[int]) -> None:
    global solver
    solver.getBest(mNos)


# import sys
# from solution import init, pickup, reset, getBest

CMD_INIT = 100
CMD_PICKUP = 200
CMD_RESET = 300
CMD_GET_BEST = 400

MAX_M = 2000

mSeed = 0


def pseudo_rand():
    global mSeed
    mSeed = (mSeed * 1103515245 + 12345) % 2147483647
    return mSeed >> 16


mXs = [0 for _ in range(MAX_M)]
mYs = [0 for _ in range(MAX_M)]


def run():
    global mSeed

    mNos = [0] * 5

    Q, mSeed = map(int, input().split())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            M = int(next(input_iter))
            L = N // 10
            for i in range(M):
                mXs[i] = pseudo_rand() % N
                mYs[i] = pseudo_rand() % N
            init(N, M, L, mXs, mYs)
            okay = True
        elif cmd == CMD_PICKUP:
            while True:
                mSX = pseudo_rand() % N
                mSY = pseudo_rand() % N
                mEX = pseudo_rand() % N
                mEY = pseudo_rand() % N
                if mSX != mEX or mSY != mEY:
                    break
            ret = pickup(mSX, mSY, mEX, mEY)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_RESET:
            mNo = int(next(input_iter))
            res = reset(mNo)
            x = int(next(input_iter))
            y = int(next(input_iter))
            mdist = int(next(input_iter))
            rdist = int(next(input_iter))
            if (
                res.mX != x
                or res.mY != y
                or res.mMoveDistance != mdist
                or res.mRideDistance != rdist
            ):
                okay = False
        elif cmd == CMD_GET_BEST:
            getBest(mNos)
            # print(f"getBest({mNos=})")
            for i in range(5):
                ans = int(next(input_iter))
                if mNos[i] != ans:
                    # print(f"{mNos[i]=} != {ans=}")
                    okay = False
        else:
            okay = False
    return okay


# sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

# T = 2


import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print("#%d %d" % (tc, score))

profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.TIME)
stats.print_stats()
