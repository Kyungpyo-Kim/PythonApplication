from typing import List


class Solver:
    def __init__(self, N: int, mLimit: int):
        self.N = N
        self.mLimit = mLimit
        self.radios = {}
        self.grid_size = mLimit // 10
        self.grid_num = N // self.grid_size + 1
        self.grid = [[[] for _ in range(self.grid_num)] for _ in range(self.grid_num)]

    def add_radio(
        self, K: int, mID: List[int], mFreq: List[int], mY: List[int], mX: List[int]
    ):
        for i in range(K):
            mid, f, x, y = mID[i], mFreq[i], mY[i], mX[i]
            self.radios[mid] = (f, x, y)
            gx, gy = x // self.grid_size, y // self.grid_size
            self.grid[gx][gy].append((mid, f, x, y))

    def get_min_power(self, mID: int, mCount: int):
        tf, tx, ty = self.radios[mID]
        tgx, tgy = tx // self.grid_size, ty // self.grid_size

        p_cnt = [0] * (self.mLimit + 1)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                gx, gy = tgx + dx, tgy + dy
                if 0 <= gx < self.grid_num and 0 <= gy < self.grid_num:
                    for mid, f, x, y in self.grid[gx][gy]:
                        if mid == mID:
                            continue
                        p = (abs(x - tx) + abs(y - ty)) * 10 + (0 if f == tf else 1000)
                        if p <= self.mLimit:
                            p_cnt[p] += 1

        ps, cnt = 0, 0
        for p in range(11, len(p_cnt)):
            if p_cnt[p] == 0:
                continue
            if cnt + p_cnt[p] > mCount:
                ps += (mCount - cnt) * p
                return ps
            else:
                ps += p * p_cnt[p]
                cnt += p_cnt[p]

        return ps


global solver


def init(N: int, mLimit: int) -> None:
    global solver
    solver = Solver(N, mLimit)


def addRadio(
    K: int, mID: List[int], mFreq: List[int], mY: List[int], mX: List[int]
) -> None:
    global solver
    solver.add_radio(K, mID, mFreq, mY, mX)


def getMinPower(mID: int, mCount: int) -> int:
    global solver
    return solver.get_min_power(mID, mCount)


# import sys
# from solution import init, addRadio, getMinPower

CMD_INIT = 0
CMD_ADDRADIO = 1
CMD_GETPOWER = 2

MAX_RADIO = 100

id = [0 for _ in range(MAX_RADIO)]
freq = [0 for _ in range(MAX_RADIO)]
my = [0 for _ in range(MAX_RADIO)]
mx = [0 for _ in range(MAX_RADIO)]


def run():
    global id, freq, my, mx
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            Limit = int(next(input_iter))
            init(N, Limit)
            okay = True
        elif cmd == CMD_ADDRADIO:
            K = int(next(input_iter))
            for i in range(0, K):
                input_iter = iter(input().split())
                id[i] = int(next(input_iter))
                freq[i] = int(next(input_iter))
                my[i] = int(next(input_iter))
                mx[i] = int(next(input_iter))
            addRadio(K, id, freq, my, mx)
        elif cmd == CMD_GETPOWER:
            mid = int(next(input_iter))
            cnt = int(next(input_iter))
            ret = getMinPower(mid, cnt)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


import cProfile
import pstats

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    # sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)

    profiler.disable()
    stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
