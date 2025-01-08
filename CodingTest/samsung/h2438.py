import heapq
from collections import defaultdict
from typing import List


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0


class Solver:
    def __init__(
        self,
        N: int,
        mWidth: int,
        mHeight: int,
        mIDs: List[int],
        mLengths: List[List[int]],
        mUpShapes: List[List[int]],
    ) -> None:
        self.N = N
        self.mWidth = mWidth
        self.mHeight = mHeight
        self.mIDs = mIDs
        self.mLengths = mLengths
        self.mUpShapes = mUpShapes

        self.indices = sorted(range(len(mIDs)), key=lambda x: mIDs[x])

        self.shapes = defaultdict(set)  # up shapes : i_n, si
        self.waters = [[self.mWidth] * self.mHeight for _ in range(self.N)]

        for i in range(self.N):
            # update shapes
            for si in range(self.mWidth - 2):
                self.shapes[tuple(self.mUpShapes[i][si : si + 3])].add((i, si))
            # update waters
            water = self.waters[i]
            for length in self.mLengths[i]:
                for j in range(length):
                    water[j] -= 1

    def checkStructures(
        self, mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]
    ) -> int:
        shape = tuple(mDownShapes)
        if shape not in self.shapes:
            return 0

        shapes = self.shapes[shape]

        cnt = 0
        for i, si in shapes:
            tmp = self.mLengths[i][si : si + 3]
            new_lens = [
                tmp[0] + mLengths[0],
                tmp[1] + mLengths[1],
                tmp[2] + mLengths[2],
            ]
            if (
                new_lens[0] - new_lens[1] >= mLengths[0]
                or new_lens[1] - new_lens[0] >= mLengths[1]
                or new_lens[1] - new_lens[2] >= mLengths[1]
                or new_lens[2] - new_lens[1] >= mLengths[2]
                or new_lens[0] > self.mHeight
                or new_lens[1] > self.mHeight
                or new_lens[2] > self.mHeight
            ):
                continue

            cnt += 1

        return cnt

    def addStructures(
        self, mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]
    ) -> int:
        for i in self.indices:
            lengths = self.mLengths[i]
            up_shapes = self.mUpShapes[i]
            for si in range(self.mWidth - 2):
                if up_shapes[si] != mDownShapes[0]:
                    continue
                if up_shapes[si + 1] != mDownShapes[1]:
                    continue
                if up_shapes[si + 2] != mDownShapes[2]:
                    continue

                tmp = lengths[si : si + 3]
                new_lens = [
                    tmp[0] + mLengths[0],
                    tmp[1] + mLengths[1],
                    tmp[2] + mLengths[2],
                ]

                if new_lens[0] > self.mHeight:
                    continue
                if new_lens[1] > self.mHeight:
                    continue
                if new_lens[2] > self.mHeight:
                    continue

                # check first and second
                if new_lens[0] - new_lens[1] >= mLengths[0]:
                    continue
                if new_lens[1] - new_lens[0] >= mLengths[1]:
                    continue

                # check second and third
                if new_lens[1] - new_lens[2] >= mLengths[1]:
                    continue
                if new_lens[2] - new_lens[1] >= mLengths[2]:
                    continue

                # update shapes
                for j in range(self.mWidth - 2):
                    self.shapes[tuple(up_shapes[j : j + 3])].remove((i, j))
                for j in range(3):
                    lengths[si + j] = new_lens[j]
                    up_shapes[si + j] = mUpShapes[j]
                for j in range(self.mWidth - 2):
                    self.shapes[tuple(up_shapes[j : j + 3])].add((i, j))

                # update waters
                water = self.waters[i]
                for j in range(3):
                    for k in range(
                        lengths[si + j] - mLengths[j],
                        lengths[si + j],
                    ):
                        water[k] -= 1

                return self.mIDs[i] * 1000 + si + 1

        return 0

    def pourIn(self, mWater: int) -> Result:
        results = []
        for i in range(self.N):
            used = 0
            for height in range(self.mHeight):
                used += self.waters[i][height]
                if used > mWater:
                    used -= self.waters[i][height]
                    height -= 1
                    break
                if used == mWater:
                    break
            height += 1
            if 0 < used <= mWater:
                heapq.heappush(results, (-height, -used, self.mIDs[i]))

        ret = Result()
        ret.ID = ret.height = ret.used = 0

        if results:
            ret.height = -results[0][0]
            ret.used = -results[0][1]
            ret.ID = results[0][2]
            return ret

        return ret

    def __pourIn(self, mWater: int) -> Result:
        results = []
        for i in range(self.N):
            low = min(self.mLengths[i])
            high = self.mHeight
            best_height = low + 1
            best_used = 0

            while low <= high:
                mid = (low + high) // 2
                tmp_used = 0
                for c in range(self.mWidth):
                    if self.mLengths[i][c] < mid:
                        tmp_used += mid - self.mLengths[i][c]
                if tmp_used > mWater:
                    high = mid - 1
                else:
                    best_height = mid
                    best_used = tmp_used
                    low = mid + 1

            if 0 < best_used <= mWater:
                heapq.heappush(results, (-best_height, -best_used, self.mIDs[i]))

        ret = Result()
        ret.ID = ret.height = ret.used = 0

        if results:
            ret.height = -results[0][0]
            ret.used = -results[0][1]
            ret.ID = results[0][2]
            return ret

        return ret


global solver


def init(
    N: int,
    mWidth: int,
    mHeight: int,
    mIDs: List[int],
    mLengths: List[List[int]],
    mUpShapes: List[List[int]],
) -> None:
    global solver
    solver = Solver(N, mWidth, mHeight, mIDs, mLengths, mUpShapes)


def checkStructures(
    mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]
) -> int:
    return solver.checkStructures(mLengths, mUpShapes, mDownShapes)


def addStructures(
    mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]
) -> int:
    return solver.addStructures(mLengths, mUpShapes, mDownShapes)


def pourIn(mWater: int) -> Result:
    return solver.pourIn(mWater)


import sys

# from solution import init, checkStructures, addStructures, pourIn


def input():
    return sys.stdin.readline().rstrip()


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0


CMD_INIT = 1
CMD_ADD = 2
CMD_CHECK = 3
CMD_POUR = 4

MAX_N = 20
MAX_WIDTH = 500


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mWidth = int(next(input_iter))
            mHeight = int(next(input_iter))
            mIDs = [int(next(input_iter)) for i in range(N)]
            mLengths_tanks = []
            for i in range(N):
                input_iter = iter(input().split())
                mLengths_tanks.append([int(next(input_iter)) for i in range(mWidth)])
            mUpShapes_tanks = []
            for i in range(N):
                input_iter = iter(input().split())
                mUpShapes_tanks.append([int(next(input_iter)) for i in range(mWidth)])
            init(N, mWidth, mHeight, mIDs, mLengths_tanks, mUpShapes_tanks)
            okay = True
        elif cmd == CMD_CHECK:
            mLengths = [int(next(input_iter)) for i in range(3)]
            mUpShapes = [int(next(input_iter)) for i in range(3)]
            mDownShapes = [int(next(input_iter)) for i in range(3)]
            ret = checkStructures(mLengths, mUpShapes, mDownShapes)
            ans = int(next(input_iter))
            # print(f"checkStructures: {ret=} {ans=}")
            if ret != ans:
                okay = False
        elif cmd == CMD_ADD:
            mLengths = [int(next(input_iter)) for i in range(3)]
            mUpShapes = [int(next(input_iter)) for i in range(3)]
            mDownShapes = [int(next(input_iter)) for i in range(3)]
            ret = addStructures(mLengths, mUpShapes, mDownShapes)
            ans = int(next(input_iter))
            # print(f"addStructures: {ret=} {ans=}")
            if ret != ans:
                okay = False
        elif cmd == CMD_POUR:
            mWater = int(next(input_iter))
            ret = pourIn(mWater)
            ans = int(next(input_iter))
            ans_height = 0
            ans_used = 0
            if ans != 0:
                ans_height = int(next(input_iter))
                ans_used = int(next(input_iter))

            # print(
            #     f"pourIn: {ret.ID=} {ret.height=} {ret.used=} {ans_height=} {ans_used=}"
            # )

            if ans != 0 and (
                (ans != ret.ID) or (ans_height != ret.height) or (ans_used != ret.used)
            ):
                okay = False
            elif ans == 0 and ret.ID != 0:
                okay = False
        else:
            okay = False

    return okay


import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

if __name__ == "__main__":
    # sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    # T = 1

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)

profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.TIME)
stats.print_stats()
